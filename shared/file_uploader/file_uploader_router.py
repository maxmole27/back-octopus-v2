import json
import os
import uuid
from typing import List

import pytesseract
from fastapi import APIRouter, Depends, File, HTTPException, UploadFile
from openai import OpenAI
from PIL import Image

from ...database import get_db
from ..utils.sanitize_file import sanitize_filename
from ..utils.sanitize_json_string import sanitize_json_string

router = APIRouter(
  prefix="/file_uploader",  
  tags=["file_uploader"],
  responses={404: {"description": "File Upload Error"}}
)

@router.post("/")
async def upload_image(file: UploadFile = File()):
    UPLOAD_DIR = "static"
    os.makedirs(UPLOAD_DIR, exist_ok=True)
    # Verifica si el archivo es una imagen
    if not file.content_type.startswith("image/"):
      raise HTTPException(status_code=400, detail="El archivo debe ser una imagen")
    sanitized_name = sanitize_filename(file.filename)
    filename = "{}-{}".format(uuid.uuid4(), sanitized_name)
    file_path = os.path.join(UPLOAD_DIR, filename)
    
    with open(file_path, "wb") as buffer:
      buffer.write(await file.read())

    return {"filename": file.filename, "path": filename}

@router.post('/tesseract')
async def upload_image_and_extract_text(file: UploadFile = File()):
    UPLOAD_DIR = "static"
    os.makedirs(UPLOAD_DIR, exist_ok=True)
    # Verifica si el archivo es una imagen
    if not file.content_type.startswith("image/"):
      raise HTTPException(status_code=400, detail="El archivo debe ser una imagen")
    sanitized_name = sanitize_filename(file.filename)
    filename = "{}-{}".format(uuid.uuid4(), sanitized_name)
    file_path = os.path.join(UPLOAD_DIR, filename)
    
    with open(file_path, "wb") as buffer:
      # Abrir la imagen y extraer texto
      img = Image.open(file.file)
      text = pytesseract.image_to_string(img)
      # buffer.write(await file.read())
    
    # NOW WE NEED TO CONSUME OPENAI API
    api_url = os.getenv("OPEN_AI_API_BASE_URL")
    api_key = os.getenv("OPEN_AI_API_KEY")
    organization = os.getenv("OPEN_AI_ORG_ID")
    project_id = os.getenv("OPEN_AI_PROJECT_ID")
    client = OpenAI(
      organization=organization,
      project=project_id,
      api_key=api_key,
    )

    completion = client.chat.completions.create(
      model="gpt-4o",
      messages=[
        {"role": "system", "content": '''you will be an sports betting expert, and your role will be get bet slips screenshots. You must be able to extract and identify all the data about this bet slip. For example: the teams/players; is a parlay?; bet amount; odds; bet status, etc. You must return data in json format, as an array (in case of parlay). I will give you the data required with examples:
        sport: Tennis, Football, American Footbal, MMA, etc.
        team1: Manchester United, Novak Djokovic, Connor McGregor, Argentina
        team2: Same examples of "Team 1"
        type_of_bet: Over/Under goals, over/under points, Handicap, 1x2, Moneyline, Over/Under Corners, Over/Under Cards, etc.
        specific_bet: Over 167.5 Points, Over 2.5 Goals, Under 9 innings, Over 12.5 corners, Manchester United +0.5, etc.
        odds: 1.83; 2.00; 1.32, etc
        bet_status: pending, won, loss, half-win/half-void, half-loss/half-void, postponed, etc.
        final_score (OPTIONAL): 3-2, 1-0, 80-160, etc.
        event_date (OPTIONAL): 2024-03-21
        event_time (OPTIONAL): 13:30
        money_stake: 10, 30, 50, 100
        potential_win: 80, 120, 100.
        You only gave the json data. You must return the data in json format 100% raw. If you don't find some of the data, you must return the field in json but with null value. 
         '''},
        {"role": "user", "content": text}
      ]
    )

    responsex = sanitize_json_string(completion.choices[0].message.content)

    print(responsex)
    # tojson = json.loads(completion.choices[0].message.content)
    data = json.loads(responsex)


    return {"filename": file.filename, "path": filename, "text": text, "completion": responsex}

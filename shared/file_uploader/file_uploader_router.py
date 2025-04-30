import json
import os
import uuid
from typing import List

import pytesseract
from dotenv import load_dotenv
from fastapi import APIRouter, Depends, File, HTTPException, UploadFile
from openai import OpenAI
from PIL import Image

from ...database import get_db
from ...shared.utils.load_prompt import load_prompt
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
    load_dotenv(override=True)
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
    api_key = os.getenv("OPEN_AI_API_KEY", "").strip()

    client = OpenAI(api_key=str(api_key))

    prompt_content = load_prompt("./shared/file_uploader/betslip_reader.txt")
    print(prompt_content)
    completion = client.chat.completions.create(
      model="gpt-4o",
      messages=[
        {"role": "system", "content": prompt_content},
        {"role": "user", "content": text}
      ]
    )

    responsex = sanitize_json_string(completion.choices[0].message.content)

    data = json.loads(responsex)


    return {"filename": file.filename, "path": filename, "text": text, "completion": responsex}

@router.post("/tesseract_multiple")
async def upload_images_and_extract_text(files: List[UploadFile] = File(...)):
  load_dotenv(override=True)
  UPLOAD_DIR = "static"
  os.makedirs(UPLOAD_DIR, exist_ok=True)
  # Verifica si el archivo es una imagen
  upload_responses = []
  print('files', files)
  for file in files:
    if not file.content_type.startswith("image/"):
      raise HTTPException(status_code=400, detail="El archivo debe ser una imagen")
    sanitized_name = sanitize_filename(file.filename)
    filename = "{}-{}".format(uuid.uuid4(), sanitized_name)
    file_path = os.path.join(UPLOAD_DIR, filename)
    
    with open(file_path, "wb") as buffer:
      # Abrir la imagen y extraer texto
      img = Image.open(file.file)
      text = pytesseract.image_to_string(img)
    api_key = os.getenv("OPEN_AI_API_KEY", "").strip()
    client = OpenAI(api_key=str(api_key))
    prompt_content = load_prompt("./shared/file_uploader/betslip_reader.txt")
    completion = client.chat.completions.create(
      model="gpt-4o",
      messages=[
        {"role": "system", "content": prompt_content},
        {"role": "user", "content": text}
      ]
    )

    responsex = sanitize_json_string(completion.choices[0].message.content)

    data = json.loads(responsex)


    upload_responses.append({"filename": file.filename, "path": filename, "text": text, "completion": responsex})

  return upload_responses
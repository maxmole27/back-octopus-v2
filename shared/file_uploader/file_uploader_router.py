import os
import uuid
from typing import List

from fastapi import APIRouter, Depends, File, HTTPException, UploadFile

from ...database import get_db
from ..utils.sanitize_file import sanitize_filename

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


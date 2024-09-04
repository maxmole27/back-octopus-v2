import os
from typing import List

from fastapi import APIRouter, Depends, File, HTTPException, UploadFile

from ...database import get_db

router = APIRouter(
  prefix="/file_uploader",
  tags=["file_uploader"],
  responses={404: {"description": "File Upload Error"}}
)

@router.get("/")
async def root():
    return {"message": "Hello World"}

@router.post("/")
async def upload_image(file: UploadFile = File()):
    UPLOAD_DIR = "uploads"
    os.makedirs(UPLOAD_DIR, exist_ok=True)
    # Verifica si el archivo es una imagen
    if not file.content_type.startswith("image/"):
      raise HTTPException(status_code=400, detail="El archivo debe ser una imagen")

    file_path = os.path.join(UPLOAD_DIR, file.filename)
    
    with open(file_path, "wb") as buffer:
      buffer.write(await file.read())

    return {"filename": file.filename, "path": file_path}


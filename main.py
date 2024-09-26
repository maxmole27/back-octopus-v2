import os
from typing import List

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from . import database
from .auth.roles import role_model, role_router
from .auth.users import user_model, user_router
from .bet_registry.systems import system_model, system_router
from .shared.bookies import bookie_model, bookie_router
from .shared.file_uploader import file_uploader_router
from .shared.sports import sport_model, sport_router

bookie_model.Base.metadata.create_all(bind=database.engine)
role_model.Base.metadata.create_all(bind=database.engine)
user_model.Base.metadata.create_all(bind=database.engine)
sport_model.Base.metadata.create_all(bind=database.engine)
system_model.Base.metadata.create_all(bind=database.engine)

load_dotenv()  # take environment variables
app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])
app.mount('/static', StaticFiles(directory='static'), name='static')
app.include_router(bookie_router.router)
app.include_router(role_router.router)
app.include_router(user_router.router)
app.include_router(sport_router.router)
app.include_router(system_router.router)
app.include_router(file_uploader_router.router)

@app.get("/")
def root():
    return {"message": "Hello World"}


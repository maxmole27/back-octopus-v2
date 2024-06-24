from typing import List

from fastapi import FastAPI

from . import database
from .auth.roles import role_model, role_router
from .auth.users import user_model, user_router
from .shared.bookies import bookie_model, bookie_router
from .shared.sports import sport_model, sport_router

bookie_model.Base.metadata.create_all(bind=database.engine)
role_model.Base.metadata.create_all(bind=database.engine)
user_model.Base.metadata.create_all(bind=database.engine)
sport_model.Base.metadata.create_all(bind=database.engine)


app = FastAPI()

app.include_router(bookie_router.router)
app.include_router(role_router.router)
app.include_router(user_router.router)
app.include_router(sport_router.router)

@app.get("/")
def root():
    return {"message": "Hello World"}


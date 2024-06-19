from typing import List

from fastapi import FastAPI

from . import database
from .auth.roles import role_model, role_router
from .shared.bookies import bookie_model, bookie_router

bookie_model.Base.metadata.create_all(bind=database.engine)
role_model.Base.metadata.create_all(bind=database.engine)


app = FastAPI()

app.include_router(bookie_router.router)
app.include_router(role_router.router)

@app.get("/")
def root():
    return {"message": "Hello World"}


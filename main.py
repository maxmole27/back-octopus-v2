import os
from typing import List

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from . import database
from .auth.roles import role_model, role_router
from .auth.users import user_model, user_router
from .bet_registry.bet_statuses import bet_status_model, bet_status_router
from .bet_registry.betslips import betslip_model, betslip_router
from .bet_registry.individual_bets import individual_bet_model
from .bet_registry.league_or_tournaments import (league_or_tournament_model,
                                                 league_or_tournament_router)
from .bet_registry.player_or_teams import (player_or_team_model,
                                           player_or_team_router)
from .bet_registry.systems import system_model, system_router
from .shared.bookies import bookie_model, bookie_router
from .shared.file_uploader import file_uploader_router
# pending router at location
from .shared.location import location_model
from .shared.sports import sport_model, sport_router

bookie_model.Base.metadata.create_all(bind=database.engine)
role_model.Base.metadata.create_all(bind=database.engine)
user_model.Base.metadata.create_all(bind=database.engine)
sport_model.Base.metadata.create_all(bind=database.engine)
system_model.Base.metadata.create_all(bind=database.engine)
betslip_model.Base.metadata.create_all(bind=database.engine)
individual_bet_model.Base.metadata.create_all(bind=database.engine)
bet_status_model.Base.metadata.create_all(bind=database.engine)
league_or_tournament_model.Base.metadata.create_all(bind=database.engine)
location_model.Base.metadata.create_all(bind=database.engine)
player_or_team_model.Base.metadata.create_all(bind=database.engine)
player_or_team_model.Base.metadata.create_all(bind=database.engine)




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
app.include_router(betslip_router.router)
app.include_router(bet_status_router.router)
app.include_router(league_or_tournament_router.router)
app.include_router(player_or_team_router.router)

@app.get("/")
def root():
    return {"message": "Hello World"}


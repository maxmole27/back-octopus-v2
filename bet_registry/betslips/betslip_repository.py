
from datetime import datetime
from typing import List, Optional, Tuple

from sqlalchemy.orm import Session, aliased
from sqlalchemy.sql.expression import and_, or_

from ..individual_bets.individual_bet_model import IndividualBet
from ..player_or_teams.player_or_team_model import PlayerOrTeam
from ..systems.system_model import System
from .betslip_model import Betslip
from .betslip_schemas import (BetslipCreate, BetslipGet, BetslipResponse,
                              BetslipUpdate)


class BetslipRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, betslip_data: BetslipCreate) -> Betslip:
        new_betslip = Betslip(
            system_id=betslip_data.system_id,
            bookie_id=betslip_data.bookie_id,
            stake=betslip_data.stake,
            money_stake=betslip_data.money_stake,
        )
        self.db.add(new_betslip)
        self.db.flush()  # Flush para obtener el ID de betslip
        return new_betslip

    def get_betslip(self, betslip_id: int) -> Betslip:
        return self.db.query(Betslip).filter(Betslip.id == betslip_id).first()
    
    def get_betslips(self, page: int, limit: int) -> List[Betslip]:
        return self.db.query(Betslip).offset(page * limit).limit(limit).all()

    def get_betslips_from_system(
        self, 
        system_id: int, 
        page: int, 
        limit: int, 
        start_date: Optional[str] = None, 
        end_date: Optional[str] = None, 
        team_name: Optional[str] = None
    ) -> Tuple[List[Betslip], int]:

        # Crear alias para evitar duplicación en los joins
        PlayerOrTeam1 = aliased(PlayerOrTeam)
        PlayerOrTeam2 = aliased(PlayerOrTeam)

        # Construir consulta base con filtros aplicados
        base_query = self.db.query(Betslip).join(Betslip.individual_bets)
        base_query = base_query.join(PlayerOrTeam1, IndividualBet.player_or_team1)
        base_query = base_query.join(PlayerOrTeam2, IndividualBet.player_or_team2)

        # Filtro por sistema
        base_query = base_query.filter(Betslip.system_id == system_id)
        
        # Procesar fechas
        if start_date:
            start_date = datetime.strptime(start_date, "%Y-%m-%d")
        if end_date:
            end_date = datetime.strptime(end_date, "%Y-%m-%d").replace(hour=23, minute=59, second=59)

        # Filtro por rango de fechas
        if start_date and end_date:
            base_query = base_query.filter(and_(Betslip.created_at >= start_date, Betslip.created_at <= end_date))

        # Filtro por nombre de equipo o jugador usando los alias
        if team_name:
            base_query = base_query.filter(
                or_(
                    PlayerOrTeam1.name.ilike(f"%{team_name}%"),
                    PlayerOrTeam2.name.ilike(f"%{team_name}%")
                )
            )

        # Obtener el total de registros aplicando los filtros, pero sin paginación
        total_count = base_query.distinct(Betslip.id).count()

        # Aplicar paginación en la consulta para obtener los registros paginados
        paginated_query = base_query.distinct(Betslip.id).offset(page * limit).limit(limit)
        betslips = paginated_query.all()

        return betslips, total_count

        
    def create_betslip(self, betslip: BetslipCreate) -> Betslip:
        db_betslip = Betslip(system_id=betslip.system_id)
        self.db.add(db_betslip)
        self.db.commit()
        self.db.refresh(db_betslip)
        return betslip
    
    def update_betslip(self, betslip_id: int, betslip: BetslipUpdate) -> Betslip:
        print('wqdqweqw',betslip)
        db_betslip = self.db.query(Betslip).filter(Betslip.id == betslip_id).first()
        db_betslip.id = betslip.id
        db_betslip.system_id = betslip.system_id
        db_betslip.bookie_id = betslip.bookie_id
        db_betslip.stake = betslip.stake
        db_betslip.money_stake = betslip.money_stake
        self.db.commit()
        self.db.refresh(db_betslip)
        return db_betslip
    
    def count_betslips(self, system_id: int) -> int:
        return self.db.query(Betslip).filter(Betslip.system_id == system_id).count()
    

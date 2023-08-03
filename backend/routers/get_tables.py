
from database.queries import F1Queries
from fastapi import APIRouter

router = APIRouter()

@router.get("/drivers")
def drivers():
    return F1Queries.get_drivers_json()

@router.get("/fastest_laps")
def laps():
    return F1Queries.get_fastest_laps_json()

@router.get("/races")
def races():
    return F1Queries.get_races_json()
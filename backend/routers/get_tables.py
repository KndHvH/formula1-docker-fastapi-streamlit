
from database.queries import F1Queries
from fastapi import APIRouter

router = APIRouter()

@router.get("/drivers")
async def drivers():
    return F1Queries.get_drivers_json()

@router.get("/fastest_laps")
async def laps():
    return F1Queries.get_fastest_laps_json()

@router.get("/races")
async def races():
    return F1Queries.get_races_json()
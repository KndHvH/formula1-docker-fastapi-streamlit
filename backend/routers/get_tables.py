from database.queries import ContentQueries
from fastapi import APIRouter

router = APIRouter()


@router.get("/drivers")
async def drivers():
    return ContentQueries.get_drivers_json()


@router.get("/fastest_laps")
async def laps():
    return ContentQueries.get_fastest_laps_json()


@router.get("/races")
async def races():
    return ContentQueries.get_races_json()

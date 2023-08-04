from database.queries import TableQueries
from fastapi import APIRouter

router = APIRouter()


@router.get("/drivers")
async def drivers():
    return TableQueries.get_drivers_json()


@router.get("/fastest_laps")
async def laps():
    return TableQueries.get_fastest_laps_json()


@router.get("/races")
async def races():
    return TableQueries.get_races_json()

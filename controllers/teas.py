from fastapi import APIRouter, HTTPException
from models.tea_data import teas_db

router = APIRouter()


@router.get("/teas")
def get_teas():
    return teas_db


@router.get("/teas/{tea_id}")
def get_single_tea(tea_id: int):
    # Get tea by ID
    for tea in teas_db["teas"]:
        if tea["id"] == tea_id:
            return tea
    # If tea with the given ID is not found
    raise HTTPException(status_code=404, detail="Tea not found")

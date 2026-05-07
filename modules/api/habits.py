from sqlalchemy.exc import IntegrityError
from fastapi import APIRouter, HTTPException, Body, Path

import pydantic

from modules.service import habits as habits_service
from modules.schemas import UserData
from modules.exceptions import UserNotFound, InvalidVerification

habits_api_router = APIRouter()

@habits_api_router.post("/habits/create")
def create_habit(data: dict = Body(
            example = {
                "title": "new habit",
            }
        )
    ) -> dict[str, str]:
    
    try:
        return habits_service.create_habit(data = data)
    
    except pydantic.ValidationError as error:
        raise HTTPException(
            status_code = 422,
            detail = error.errors()
        )
    
    except IntegrityError:
        raise HTTPException(
            status_code = 409,
            detail = "Error during habit query"
        )
    
@habits_api_router.get("/habits")
def get_habits():
    try:
        return habits_service.get_habits()
    
    except pydantic.ValidationError as error:
        raise HTTPException(
            status_code = 422,
            detail = error.errors()
        )

@habits_api_router.get("/habits/{id}")
def get_habit(id: int = Path(example = 1)):
    try:
        return habits_service.get_habit(id = id)
    except pydantic.ValidationError as error:
        raise HTTPException(
            status_code = 422,
            detail = error.errors()
        )
    
@habits_api_router.delete("/habits/{id}")
def delete_habit(id: int = Path(example = 1)):

    return habits_service.delete_habit(id = id)
    
from fastapi import APIRouter, Body, Query
import modules.service as service
from .schemas import UserData


api_router = APIRouter()


@api_router.post("/add_user")
def add_user(data: dict = Body(
            example = {
                "first_name": "Jason",
                "last_name": "Statham",
                "email": "js1404@gmail.com"
            }
        )
    ) -> UserData:
    
    return service.add_user(data = data)

@api_router.get("/get_user")
def get_user(id: int = Query(example = 1)) -> UserData:
    
    return service.get_user(id = id)


@api_router.get("/get_all_users")
def get_all_users() -> list:
    
    return service.get_all_users()

from fastapi import APIRouter, Body, Query
from modules.service import user as user_service
from modules.schemas import UserData

user_api_router = APIRouter()

@user_api_router.post("/add_user")
def add_user(data: dict = Body(
            example = {
                "first_name": "Jason",
                "last_name": "Statham",
                "email": "js1404@gmail.com"
            }
        )
    ) -> UserData:
    
    pass
    # return user_service.add_user(data = data)


@user_api_router.get("/get_user")
def get_user(id: int = Query(example = 1)) -> UserData:
    
    pass
    # return user_service.get_user(id = id)


@user_api_router.get("/get_all_users")
def get_all_users() -> list:
    
    pass
    # return user_service.get_all_users()

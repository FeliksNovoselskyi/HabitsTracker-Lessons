from fastapi import APIRouter, Body, Query
from modules.service import account as account_service
from modules.schemas import UserData

account_api_router = APIRouter()

@account_api_router.post("/sign_up")
def sign_up(data: dict = Body(
            example = {
                "first_name": "Jason",
                "last_name": "Statham",
                "email": "js1404@gmail.com",
                "password": "A0000000"
            }
        )
    ) -> dict[str, str]:
    
    return account_service.sign_up(data = data)

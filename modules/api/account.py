from fastapi import APIRouter, HTTPException, Body, Query
from modules.service import account as account_service
from modules.schemas import UserData
from modules.exceptions import UserNotFound, InvalidVerification

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

@account_api_router.post("/login")
def login(data: dict = Body(
            example = {
                "email": "js1404@gmail.com",
                "password": "A0000000"
            }
        )
    ) -> dict[str, str]:
    
    try:
        return account_service.login(data = data)
    
    except UserNotFound as error:
        raise HTTPException(
            status_code = error.CODE,
            detail = error.DETAIL,
        )
    
    except InvalidVerification as error:
        raise HTTPException(
            status_code = error.CODE,
            detail = error.DETAIL,
        )

from fastapi import APIRouter, HTTPException
from .repository import add_user
from .schemas import UserData


api_router = APIRouter()


@api_router.post("/add_user")
def user_info(data: dict):
    
    try:    
        user_data = UserData(
            first_name = data["first_name"],
            last_name = data["last_name"],
            email = data["email"]
        )
        
        add_user(data = data)
        return user_data
    except:
        raise HTTPException(status_code = 400, detail = "Invalid fields")

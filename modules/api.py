from fastapi import APIRouter, HTTPException, Body, Query
from .repository import add_user, get_user
from .schemas import UserData



api_router = APIRouter()


@api_router.post("/add_user")
def user_info(data: dict = Body(
            example = {
                "first_name": "Jason",
                "last_name": "Statham",
                "email": "js1404@gmail.com"
            }
        )
    ):
    
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

@api_router.get("/get_user")
def user_info(id: int = Query(example = 1)):
    
    try:    
        user = get_user(id = id)
        return user
    except:
        raise HTTPException(status_code = 400, detail = "Invalid fields")
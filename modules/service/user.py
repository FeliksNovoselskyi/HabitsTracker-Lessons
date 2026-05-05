from fastapi import HTTPException

from modules.repository import user as user_repository
from modules.schemas import UserData

def get_user(id: int):
    try:    
        user_data_dict = user_repository.get_user(id = id)
        
        print(user_data_dict["first_name"])
        
        user_data = UserData(
            first_name = user_data_dict["first_name"],
            last_name = user_data_dict["last_name"],
            email = user_data_dict["email"]
        )
        
        return user_data
    
    except:
        raise HTTPException(status_code = 400, detail = "Invalid fields")

def add_user(data: dict):
    try:    
        user_data = UserData(
            first_name = data["first_name"],
            last_name = data["last_name"],
            email = data["email"]
        )
        
        user_repository.add_user(data = data)
        return user_data
    except:
        raise HTTPException(status_code = 400, detail = "Invalid fields")

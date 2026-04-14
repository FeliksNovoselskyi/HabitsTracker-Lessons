import modules.repository as repository
from .schemas import UserData
from fastapi import HTTPException

def get_user(id: int):
    try:    
        user_data_dict = repository.get_user(id = id)
        
        print(user_data_dict["first_name"])
        
        user_data = UserData(
            first_name = user_data_dict["first_name"],
            last_name = user_data_dict["last_name"],
            email = user_data_dict["email"]
        )
        
        return user_data
    
    except:
        raise HTTPException(status_code = 400, detail = "Invalid fields")

def get_all_users():

    users_list = repository.get_all_users()
    
    filtered_users_list = []
    try:
        for user in users_list:
            user_data = UserData(
                first_name = user.first_name,
                last_name = user.last_name,
                email = user.email
            )
            filtered_users_list.append(user_data)
        
        return filtered_users_list
    
    except:
        raise HTTPException(status_code = 400, detail = "Invalid fields")

def add_user(data: dict):
    try:    
        user_data = UserData(
            first_name = data["first_name"],
            last_name = data["last_name"],
            email = data["email"]
        )
        
        repository.add_user(data = data)
        return user_data
    except:
        raise HTTPException(status_code = 400, detail = "Invalid fields")

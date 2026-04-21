from fastapi import HTTPException
import pwdlib

from modules.repository import account as account_repository
from modules.schemas import UserData

password_hasher = pwdlib.PasswordHash.recommended()

def sign_up(data: dict):
    
    if not data:
        raise HTTPException(status_code = 400, detail="Empty request body")
    
    password = password_hasher.hash(data["password"])
    
    user_data = UserData(
        first_name = data["first_name"],
        last_name = data["last_name"],
        email = data["email"],
        password = password
    )
    
    account_repository.sign_up(user_data = user_data)
    
    return {
        "message": "Successful signup"
    }

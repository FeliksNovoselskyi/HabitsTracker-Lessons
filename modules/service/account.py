from fastapi import HTTPException
import pwdlib

from modules.exceptions import UserNotFound, InvalidVerification
from modules.repository import account as account_repository
from modules.schemas import UserData, UserLoginData
from modules.jwt.functions import encode_jwt

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

def login(data: dict):
    
    if not data:
        raise HTTPException(status_code = 400, detail="Empty request body")
    
    # Проверку типов данных
    user_login_data = UserLoginData(
        email = data["email"],
        password = data["password"]
    )
    
    # Проверка получения пользователя
    user: dict = account_repository.get_user(email = user_login_data.email)
    
    if not user:
        raise UserNotFound(
            code = 401,
            detail = 'not found'
        )
    
    # Проверка хеша введенного пароля с пользовательским
    password_verify = password_hasher.verify(password = user_login_data.password, hash = user['password'])
    
    if not password_verify:
        raise InvalidVerification(
            code = 401,
            detail = 'Invalid verification'
        )
    
    access_token = encode_jwt(user_id = user['id'])
    
    return {
        "access_token": access_token,
        "token_type": "bearer"
    }
    

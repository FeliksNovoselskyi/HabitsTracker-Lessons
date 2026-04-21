from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError

from modules.db import sessionmaker, User
from modules.schemas import UserData

def sign_up(user_data: UserData):
    with sessionmaker.begin() as session:
        try:    
            user = User(
                first_name = user_data.first_name,
                last_name = user_data.last_name,
                email = user_data.email,
                password = user_data.password
            )
            session.add(user)
            session.commit()
            
        except IntegrityError:
            raise 

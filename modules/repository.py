from fastapi import HTTPException
from .db import sessionmaker, User

def add_user(data: dict):
    
    with sessionmaker.begin() as session:
        try:    
            user = User(
                first_name = data["first_name"],
                last_name = data["last_name"],
                email = data["email"]
            )
            session.add(user)
            session.commit()
            
        except:
            raise HTTPException()
        

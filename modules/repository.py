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

def get_user(id: int):
    with sessionmaker.begin() as session:
        try:
            selected = session.query(User).where(User.id == id)
            user = selected.scalar()
            user = User(
                first_name = user.first_name,
                last_name = user.last_name,
                email = user.email
            )
            return user     
        except:
            raise HTTPException()
        

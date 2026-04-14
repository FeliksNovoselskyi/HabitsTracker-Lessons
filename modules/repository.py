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
            user: User = selected.scalar()
            
            return {
                "first_name": user.first_name,
                "last_name": user.last_name,
                "email": user.email
            }
        
        except:
            raise HTTPException()

def get_all_users():
    with sessionmaker.begin() as session:
        try:
            users_list = session.query(
                User.id, User.first_name, User.last_name, User.email
            ).all()
            
            return users_list   
        except:
            raise HTTPException()
        

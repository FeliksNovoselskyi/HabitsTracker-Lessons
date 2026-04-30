from sqlalchemy.exc import IntegrityError

from modules.db import sessionmaker, User
from modules.schemas import UserData
from modules.exceptions import UserNotFound

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


def get_user(email: str):
    with sessionmaker.begin() as session:
        selected = session.query(User).where(User.email == email)
        user: User = selected.scalar()
        
        if not user:
            raise UserNotFound(code = 404, detail = "User not found")
        
        return {
            'id': user.id,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
            "password": user.password
        }

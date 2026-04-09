from sqlalchemy import Column, Integer, String
from ..settings import base_model


class User(base_model):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key = True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from ..settings import base_model

class Habit(base_model):
    __tablename__ = "habits"

    id = Column(Integer, primary_key = True)
    title = Column(String, unique = True, nullable = False)
    
    habit_logs = relationship("HabitLog", cascade="all, delete-orphan")

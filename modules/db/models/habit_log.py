from sqlalchemy import Column, Integer, String, Date, Boolean, ForeignKey
from ..settings import base_model

class HabitLog(base_model):
    __tablename__ = "habit_logs"

    id = Column(Integer, primary_key = True)
    
    habit_id = Column(Integer, ForeignKey("habits.id", ondelete="CASCADE"), nullable = False)
    date = Column(Date, unique = True, nullable = False)
    is_done = Column(Boolean, default = False)
    


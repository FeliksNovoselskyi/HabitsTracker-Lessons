from sqlalchemy.exc import IntegrityError

from modules.db import sessionmaker, Habit
from modules.schemas import HabitData
from modules.exceptions import HabitNotFound

def create_habit(habit_data: HabitData):
    with sessionmaker.begin() as session:
        try:    
            habit = Habit(
                title = habit_data.title
            )
            session.add(habit)
            session.commit()
            
        except IntegrityError:
            raise

def get_habits():
    with sessionmaker.begin() as session:
        try:
            habits_list = session.query(
                Habit.id, Habit.title
            ).all()
            
            return habits_list  
        
        except:
            raise HabitNotFound(
                code = 404, 
                detail = "Habit not found"
            )

def get_habit(id: int):
    with sessionmaker.begin() as session:
        try:
            selected = session.query(Habit).where(Habit.id == id)
            habit: Habit = selected.scalar()
            
            return {
                "title": habit.title,
            }
        
        except:
            raise HabitNotFound(
                code = 404, 
                detail = "Habit not found"
            )

def delete_habit(id: int):
    with sessionmaker.begin() as session:
        habit_to_delete = session.get(Habit, id)

        if not habit_to_delete:
            raise HabitNotFound(
                code = 404, 
                detail = "Habit not found"
            )

        session.delete(habit_to_delete)
        session.commit()
        

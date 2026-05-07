from fastapi import HTTPException
import pwdlib

from modules.exceptions import EmptyRequestBody, InvalidFields
from modules.repository import habits as habits_repository
from modules.schemas import HabitData
from modules.jwt.functions import encode_jwt


def create_habit(data: dict):
    
    if not data:
        raise EmptyRequestBody(status_code = 400, detail="Empty request body")
    
    habit_data = HabitData(
        title = data["title"]
    )
    
    habits_repository.create_habit(habit_data = habit_data)
    
    return {
        "message": "Habbit created"
    }

def get_habits():
    habits_list = habits_repository.get_habits()
    
    filtered_habits_list = []
    try:
        for habit in habits_list:
            user_data = HabitData(
                title = habit.title
            )
            filtered_habits_list.append(user_data)
        
        return filtered_habits_list
    
    except:
        raise InvalidFields(status_code = 400, detail = "Invalid fields")

def get_habit(id: int):
    try:    
        habit_data_dict = habits_repository.get_habit(id = id)
        
        habit_data = HabitData(
            title = habit_data_dict["title"]
        )
        
        return habit_data
    
    except:
        raise InvalidFields(status_code = 400, detail = "Invalid fields")

def delete_habit(id: int):
    try:   
        habits_repository.delete_habit(id = id)
    except:
        raise InvalidFields(status_code = 400, detail = "Invalid fields")

    return {
        "message": "Habbit deleted"
    }


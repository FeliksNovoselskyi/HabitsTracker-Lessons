import uvicorn
from fastapi import FastAPI
from modules import engine, base_model, api_router

"""
Обработать POST запрос на сохранение в БД пользователя (id, first_name, last_name, email)
Обработать GET запрос на получение его данных

Отдельно обработка запросов
Отдельно работа с БД
"""

app = FastAPI()

app.include_router(router = api_router, tags = ["User"])

if __name__ == "__main__":
    base_model.metadata.create_all(bind = engine)
    uvicorn.run(app = app)

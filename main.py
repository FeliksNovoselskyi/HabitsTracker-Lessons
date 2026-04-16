import uvicorn
from fastapi import FastAPI
from modules.db import engine, base_model
from modules.api import api_router

app = FastAPI()

app.include_router(router = api_router, tags = ["User"])

if __name__ == "__main__":
    base_model.metadata.create_all(bind = engine)
    uvicorn.run(app = app)

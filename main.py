import uvicorn
from fastapi import FastAPI
from modules.db import engine, base_model
from modules.api import user_api_router, account_api_router

app = FastAPI()

app.include_router(router = user_api_router, tags = ["User"])
app.include_router(router = account_api_router, tags = ["Account"])

if __name__ == "__main__":
    base_model.metadata.create_all(bind = engine)
    uvicorn.run(app = app)

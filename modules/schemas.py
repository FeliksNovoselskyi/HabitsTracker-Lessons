import pydantic

class UserData(pydantic.BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str

class UserLoginData(pydantic.BaseModel):
    email: str
    password: str

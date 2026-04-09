import pydantic

class UserData(pydantic.BaseModel):
    first_name: str
    last_name: str
    email: str

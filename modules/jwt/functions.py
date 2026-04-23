import jwt
import time

from fastapi import HTTPException
from datetime import datetime, timezone, timedelta
from modules.config import SECRET_KEY, ALGORITHM


def encode_jwt(user_id):
    
    expire_date = datetime.now(timezone.utc) + timedelta(minutes = 15)
    
    payload = {
        "user_id": user_id,
        "expire_date": expire_date
    }
    
    try:
        access_token = jwt.encode(
            payload = payload,
            key = SECRET_KEY,
            algorithm = ALGORITHM
        )
        
        return access_token
    
    except Exception:
        raise HTTPException(status_code = 500, detail = "Access token generation error")

def decode_jwt():
    pass

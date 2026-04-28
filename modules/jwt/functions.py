import jwt
import time

from fastapi import HTTPException
from datetime import datetime, timezone, timedelta
from modules.config import SECRET_KEY, ALGORITHM


def encode_jwt(user_id):
    
    expire_date = datetime.now(timezone.utc) + timedelta(minutes = 15)
    
    payload = {
        "user_id": user_id,
        "exp": expire_date
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

def decode_jwt(access_token):
    
    try:
        payload = jwt.decode(
            jwt = access_token,
            key = SECRET_KEY,
            algorithms = [ALGORITHM]
        )
        
        expire_date = payload['exp']
        
        time_now = time.time()

        if time_now > expire_date:
            return {
                "message": "Access token expired"
            }
        
        return payload
    
    except Exception:
        return {}



from fastapi import HTTPException, Request 
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from modules.jwt.functions import decode_jwt



class CheckUser(HTTPBearer):
    def __init__(self):
        super().__init__()
    
    async def __call__(self, request: Request):

        credentials: HTTPAuthorizationCredentials =  await super().__call__(request)

        if not credentials:
            raise HTTPException(
                status_code = 403,
                detail = 'Invalid cerdentials'
            )

        if credentials.scheme != 'Bearer':
            raise HTTPException(
                status_code = 403,
                detail = 'Invalid authentication scheme'
            )

        payload = decode_jwt(credentials.credentials)
        if not payload and "message" in payload.keys():
            raise HTTPException(
                status_code = 403,
                detail = 'Invalid credentials'
            )

        return credentials.credentials

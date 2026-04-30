from fastapi import HTTPException, Request
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from modules.jwt.functions import decode_jwt


class CheckUser(HTTPBearer):
    def __init__(self):
        super().__init__()
        
    async def __call__(self, request: Request):
        
        # Вызываем родительский метод .__call__() для получения кредов из запроса
        credentials: HTTPAuthorizationCredentials = await super().__call__(request)
        
        # Проверяем наличие кредов
        if not credentials:
            raise HTTPException(
                status_code = 403,
                detail = 'Inavalid credentials'
            ) 
        
        # Проверяем тип токена (нужен Bearer)
        if credentials.scheme != 'Bearer':
            raise HTTPException(
                status_code = 403,
                detail = 'Invalid authentication scheme'
            ) 
        payload = decode_jwt(credentials.credentials)
        
        # Проверяем сам токен
        if not payload and "message" in payload.keys():
            raise HTTPException(
                status_code = 403,
                detail = 'Inavalid credentials'
            )
        return credentials.credentials

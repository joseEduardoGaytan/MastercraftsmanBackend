import jwt

from datetime import datetime, timedelta
from fastapi import HTTPException, status
from conf import settings
from exceptions import AuthTokenMissing, AuthTokenExpired, AuthTokenCorrupted
from dotenv import dotenv_values

config = dotenv_values(".env")

SECRET_KEY = config['JWT_SECRET_KEY']
ALGORITHM = config['JWT_ALGORITHM']


def generate_access_token(
        data: dict,
        expires_delta: timedelta = timedelta(
            minutes=settings.ACCESS_TOKEN_DEFAULT_EXPIRE_MINUTES
        )
):

    expire = datetime.utcnow() + expires_delta
    token_data = {
        'id': data['id'],
        'user_type': data['user_type'],
        'exp': expire,
        'name': data['username'],
        'email': data['email'],
        'banned': data['banned']
    }

    encoded_jwt = jwt.encode(token_data, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def decode_access_token(authorization: str = None):
    if not authorization:
        raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail='Auth token is missing in headers.'                    
                )        
    
    try:                                       
        token = authorization.replace('Bearer ','')                
        payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)                
        return payload
    except jwt.exceptions.ExpiredSignatureError:
        raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail='Auth token is expired.'                    
                )        
    except jwt.exceptions.DecodeError:
         raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail='Auth token is corrupted.'                    
                )        


def generate_request_header(token_payload):    
    return {'request-user-id': str(token_payload.get("id"))}


def is_admin_user(token_payload):
    if token_payload is not None:   
        payload = decode_access_token(token_payload.get("access_token"))                  
        return payload['user_type'] == 'admin'
    return False


def is_default_user(token_payload):
    return token_payload['user_type'] in ['default', 'admin']

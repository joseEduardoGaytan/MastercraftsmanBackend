import jwt

from datetime import datetime, timedelta

from conf import settings
from exceptions import AuthTokenMissing, AuthTokenExpired, AuthTokenCorrupted


SECRET_KEY = 'e0e5f53b239df3dc39517c34ae0a1c09d1f5d181dfac1578d379a4a5ee3e0ef5'
ALGORITHM = 'HS256'


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
        raise AuthTokenMissing('Auth token is missing in headers.')

    #token = authorization.replace('Bearer ', '')
    try:                                       
        token = authorization.replace('Bearer ','')                
        payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)                
        return payload
    except jwt.exceptions.ExpiredSignatureError:
        raise AuthTokenExpired('Auth token is expired.')
    except jwt.exceptions.DecodeError:
        raise AuthTokenCorrupted('Auth token is corrupted.')


def generate_request_header(token_payload):    
    return {'request-user-id': str(token_payload.get("id"))}


def is_admin_user(token_payload):    
    payload = decode_access_token(token_payload.get("access_token"))                  
    return payload['user_type'] == 'admin'

# def is_admin_user(token_payload):          
#     return token_payload['user_type'] == 'admin'


def is_default_user(token_payload):
    return token_payload['user_type'] in ['default', 'admin']

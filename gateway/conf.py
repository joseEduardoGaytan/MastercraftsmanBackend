from dotenv import dotenv_values
from pydantic_settings import BaseSettings

config = dotenv_values(".env")

class Settings(BaseSettings):
    ACCESS_TOKEN_DEFAULT_EXPIRE_MINUTES: int = config['JWT_TOKEN_LIFETIME']
    USERS_SERVICE_URL: str = config['USERS_SERVICE_URL']        
    CONTRACTORS_SERVICE_URL: str = config['CONTRACTORS_SERVICE_URL']        
    GATEWAY_TIMEOUT: int = config['GATEWAY_TIMEOUT']

settings = Settings()

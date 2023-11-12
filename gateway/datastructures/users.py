from pydantic import BaseModel
from typing import Optional


class UsernamePasswordForm(BaseModel):
    username: str
    password: str


class UserForm(UsernamePasswordForm):
    username: str
    email: str
    address: str
    first_name: str 
    last_name: str
    state_province: str
    city: str
    country: str
    zip_code: str
    hashed_password: str = None
    user_type: str
    banned: int
    profile_picture : str =  None 


class UserUpdateForm(BaseModel):
    username: str 
    email: str 
    address: str 
    first_name: str 
    last_name: str 
    state_province: str 
    city: str 
    country: str 
    zip_code: str 
    hashed_password: str = None
    user_type: str 
    banned: int = None
    profile_picture : str =  None 


class LoginResponse(BaseModel):
    access_token: str
    token_type: str


class UserResponse(BaseModel):        
    username: str = None
    email: str = None
    address: str = None
    first_name: str = None
    last_name: str = None
    state_province: str = None
    city: str = None
    country: str = None
    zip_code: str = None    
    user_type: str = None
    banned: int = None
    profile_picture: str = None
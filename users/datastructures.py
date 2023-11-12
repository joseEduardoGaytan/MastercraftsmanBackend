from pydantic import BaseModel
from typing import Optional


class UsernamePasswordForm(BaseModel):
    username: str
    password: str


class UserForm(UsernamePasswordForm):    
    email: str
    address: str
    first_name: str 
    last_name: str 
    state_province: str
    city: str
    country: str
    zip_code: str    
    user_type: str
    banned: int
    profile_picture : str =  None 


class UserUpdateForm(BaseModel):    
    username: Optional[str] 
    email: str 
    address: str
    first_name: str 
    last_name: str 
    state_province: str 
    city: str 
    country: str 
    zip_code: str 
    hashed_password: Optional[str]
    user_type: str 
    banned: int = None
    profile_picture : Optional[str] 



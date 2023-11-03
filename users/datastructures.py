from pydantic import BaseModel
from typing import Optional


class UsernamePasswordForm(BaseModel):
    username: str
    password: str


class UserForm(UsernamePasswordForm):    
    email: str
    address: str
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
    state_province: str 
    city: str 
    country: str 
    zip_code: str 
    hashed_password: Optional[str]
    user_type: str 
    banned: int = None
    profile_picture : Optional[str] 


class UserInDb(BaseModel):
    id: int
    username: str
    email: str = None
    full_name: str = None
    user_type: str
    hashed_password: str
    created_by: int

class UserInDbChk(BaseModel):
    id: int = None
    username: str
    email: str
    address: str
    state_province: str
    city: str
    country: str
    zip_code: str
    hashed_password: str
    user_type: str
    banned: int
    profile_picture : str =  None 
from pydantic import BaseModel


class UsernamePasswordForm(BaseModel):
    username: str
    password: str


class UserForm(UsernamePasswordForm):
    username: str
    email: str
    address: str
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
    #id: int
    username: str = None
    email: str = None
    address: str = None
    state_province: str = None
    city: str = None
    country: str = None
    zip_code: str = None
    #hashed_password: str
    user_type: str = None
    banned: int = None
    profile_picture: str = None
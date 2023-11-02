
from db import engine, session
from datastructures import UserInDbChk
from models import User


def get_all_users():
    user_list = session.query(User).filter(User.banned==0).all()
    return user_list

def get_user_by_username(user_name:  str):    
    user = session.query(User).filter(User.username == user_name).first()    
    if user:
        return user
    return None

def insert_user(data: dict):    
    new_user = User(**data)    
    session.add(new_user)
    session.commit()
    session.refresh(new_user)     
    return new_users


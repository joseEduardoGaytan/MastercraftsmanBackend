
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
    
def get_user_by_id(user_id: int):
    user = session.query(User).filter(User.id == user_id).first()    
    if user:
        return user
    return None

def update_user_in_db(user_id: int, data: dict):
    user_in_db = get_user_by_id(user_id)
    if user_in_db:
        for attribute, value in data:
            if value is not None:
                setattr(user_in_db, attribute, value)        
        session.add(user_in_db)        
        session.commit()
        session.refresh(user_in_db)
    else:
        return None
    return user_in_db

def insert_user(data: dict):    
    new_user = User(**data)    
    session.add(new_user)
    session.commit()
    session.refresh(new_user)     
    return new_users

def delete_user_in_db(user_id: int):
    user_in_db = get_user_by_id(user_id)
    if user_in_db:
        session.delete(user_in_db)
        session.commit()
        return True
    return False




from db import engine, session
from datastructures import UserInDbChk
from models import users, Todo

def get_all_users():
    with engine.connect() as conn :    
        users_list = conn.execute(users.select().where(users.c.banned == 0)).fetchall()
        for user in users_list:
            yield(UserInDbChk(** user._asdict()))

def get_user_by_username(user_name:  str):
    with engine.connect() as conn :
        user = conn.execute(users.select().where(users.c.username==user_name)).fetchone()    
        if user :
            return user
    return None

def insert_user(data: dict):
    new_user = UserInDbChk(**data)
    todo1 = Todo(text="learn fastapi", is_done=True)
    todo2 = Todo(text="learn django")

    session.add_all([todo1, todo2])
    session.commit()
    # session.add(users.insert().values(
    #         id=None,            
    #         username=new_user.username,
    #         email= new_user.email,
    #         address= new_user.address,
    #         state_province= new_user.state_province,
    #         city= new_user.city,
    #         country= new_user.country,
    #         zip_code= new_user.zip_code,
    #         hashed_password= new_user.hashed_password,
    #         user_type= new_user.user_type,
    #         banned= new_user.banned,
    #         profile_picture = new_user.profile_picture)) 
    session.commit()           
    # with engine.connect() as conn:        
    #     try:
    #         res = conn.execute(users.insert().values(dict(new_user)            
    #         # id=None,            
    #         # username=new_user.username,
    #         # email= new_user.email,
    #         # address= new_user.address,
    #         # state_province= new_user.state_province,
    #         # city= new_user.city,
    #         # country= new_user.country,
    #         # zip_code= new_user.zip_code,
    #         # hashed_password= new_user.hashed_password,
    #         # user_type= new_user.user_type,
    #         # banned= new_user.banned,
    #         # profile_picture = new_user.profile_picture
    #         ))
    #         print(res)
    #     except Exception as e:
    #         print(e , "exception was rises")           
    #     user = get_user_by_username(new_user.username)
    #     print(type(user),"USER AFTER INSERT")
    #     if user:
    #         return UserInDbChk(** user._asdict())    
    return None
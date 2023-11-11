
from datastructures import UserInDb
from models import User, User_Pydantic, UserIn_Pydantic


async def get_all_users():
    user_list = await UserIn_Pydantic.from_queryset(User.all())    
    return user_list

async def get_user_by_username(user_name:  str):
    user_exists = await User.get_or_none(username=user_name).exists()    
    if user_exists:        
        return await User_Pydantic.from_queryset_single(User.get(username=user_name))            
    return None
    
async def get_user_by_id(user_id: int):
    user_exists = await User.get_or_none(id=user_id).exists()    
    if user_exists:        
        return await User_Pydantic.from_queryset_single(User.get(id=user_id))            
    return None

#TODO validate attributes id and username not in data/or duplicate username
async def update_user_in_db(user_id: int, data: User_Pydantic):
    user_exists = await User.get_or_none(id=user_id).exists()
    if user_exists:                                           
        await User.filter(id=user_id).update(**data.dict(exclude_none=True,exclude_unset=True))        
        return await get_user_by_id(user_id)                     
    else:
        return None
    
async def insert_user(data: dict):           
    user_obj = await User.create(**data)    
    return await User_Pydantic.from_tortoise_orm(user_obj)

async def delete_user_in_db(user_id: int):
    user_exists = await User.get_or_none(id=user_id).exists()
    if not user_exists:                                                
        return False
    return await User.filter(id=user_id).delete()
    



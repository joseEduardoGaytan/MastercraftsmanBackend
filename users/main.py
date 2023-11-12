from fastapi import FastAPI, HTTPException, status, Request, Response, Header
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from auth import verify_password, get_password_hash
from datastructures import UsernamePasswordForm, UserForm, UserUpdateForm
from tortoise.contrib.fastapi import register_tortoise

from dao import get_all_users, get_user_by_username, insert_user, get_user_by_id, update_user_in_db, delete_user_in_db

app = FastAPI()


origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post('/api/login', status_code=status.HTTP_201_CREATED)
async def login(form_data: UsernamePasswordForm):        
    user_in_db = await get_user_by_username(form_data.username)    
    if user_in_db ==  None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Invalid credentials',
        )
    verified = verify_password(form_data.password, user_in_db.hashed_password)
    if not verified :
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Invalid credentials',
        )
    return user_in_db


@app.post('/api/users', status_code=status.HTTP_201_CREATED)
async def create_user(user: UserForm,
                      request: Request, response: Response,
                      request_user_id: str = Header(None)):

    user_in_db = await get_user_by_username(user.username)        
    if user_in_db:        
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail='There is already another user with this username.',
        )

    hashed_password = get_password_hash(user.password)    
    data = user.dict()
    data['hashed_password']=hashed_password    
    data.pop('password')    
    user_in_db = await insert_user(data)    
    
    return user_in_db

@app.get('/api/users', status_code=status.HTTP_200_OK)
async def get_users(request: Request, response: Response,
                    request_user_id: str = Header(None)):    
    users_list = await get_all_users()    
    return users_list    


@app.get('/api/users/{user_id}', status_code=status.HTTP_200_OK)
async def get_user(user_id: int, request: Request, response: Response,
                   request_user_id: str = Header(None)):

    user_in_db = await get_user_by_id(user_id)
    if not user_in_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='User not found.',
        )
    return user_in_db


@app.delete('/api/users/{user_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id: int, request: Request, response: Response,
                      request_user_id: str = Header(None)):
    deleted = await delete_user_in_db(user_id)    
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='User cannot be deleted',
        )
    else:
        return JSONResponse(content={"message":'user has been deleted'}) 
        
@app.put('/api/users/{user_id}', status_code=status.HTTP_200_OK)
async def update_user(user_id: int, user: UserUpdateForm,
                      request: Request, response: Response,
                      request_user_id: str = Header(None)):
    
    user_in_db = await get_user_by_id(user_id)    
    if user_in_db == None:        
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail='User not found')
    user_in_db = await update_user_in_db(user_id,user)        
    return user_in_db

register_tortoise(
    app,
    db_url='mysql://master:craft@db:3306/demo',
    modules={'models': ['models']},
    generate_schemas=True,
    add_exception_handlers=True,
)

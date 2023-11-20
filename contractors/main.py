from fastapi import FastAPI, HTTPException, status, Request, Response, Header
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from tortoise.contrib.fastapi import register_tortoise
from dotenv import dotenv_values
from dao import get_all_contractors


config = dotenv_values(".env")
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

#enpints hire
@app.get('/api/contractors', status_code=status.HTTP_200_OK)
async def get_contractors(request: Request, response: Response,
                    request_user_id: str = Header(None)):
    contractor_list = await get_all_contractors()    
    return contractor_list
    


register_tortoise(
    app,
    db_url=config['DB_URL'],
    modules={'models': ['models']},
    generate_schemas=True,
    add_exception_handlers=True,
)
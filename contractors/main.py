from fastapi import FastAPI, HTTPException, status, Request, Response, Header
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from tortoise.contrib.fastapi import register_tortoise
from dotenv import dotenv_values
from datastructures import ContractorsForm
from dao import get_all_contractors, insert_contractor


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

@app.get('/api/contractors', status_code=status.HTTP_200_OK)
async def get_contractors(request: Request, response: Response,
                    request_user_id: str = Header(None)):
    contractor_list = await get_all_contractors()    
    return contractor_list

@app.post('/api/contractors', status_code=status.HTTP_201_CREATED)
async def create_contractor(contractor: ContractorsForm,
                      request: Request, response: Response,
                      request_user_id: str = Header(None)):        
    contractor = await insert_contractor(contractor.dict())        
    return contractor

register_tortoise(
    app,
    db_url=config['DB_URL'],
    modules={'models': ['models']},
    generate_schemas=True,
    add_exception_handlers=True,
)
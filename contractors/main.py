from fastapi import FastAPI, HTTPException, status, Request, Response, Header
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from tortoise.contrib.fastapi import register_tortoise
from dotenv import dotenv_values
from datastructures import ContractorsForm
from dao import get_all_contractors, insert_contractor, get_contractor_by_id


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
async def create_contractors(contractor: ContractorsForm,request: Request, response: Response,request_user_id: str = Header(None)):        
    contractor = await insert_contractor(contractor.dict())        
    return contractor

@app.get('/api/contractors/{contractor_id}', status_code=status.HTTP_200_OK)
async def get_contractors(contractor_id: int, request: Request, response: Response, request_contractor_id: str = Header(None)):
    contractor = await get_contractor_by_id(contractor_id)     
    if not contractor:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Contractor not found.',
        )
    return contractor

@app.put('/api/contractors/{contractor_id}', status_code=status.HTTP_200_OK)
async def update_contractors(contractor_id: int, contractor_form: ContractorsForm,
                      request: Request, response: Response,
                      request_contractor_id: str = Header(None)):
    print(contractor_form, "form data")
    contractor = await get_contractor_by_id(contractor_id)    
    if contractor == None:        
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail='Contractor not found')
    contractor = await update_contractor(contractor_id,contractor_form)        
    return contractor



register_tortoise(
    app,
    db_url=config['DB_URL'],
    modules={'models': ['models']},
    generate_schemas=True,
    add_exception_handlers=True,
)
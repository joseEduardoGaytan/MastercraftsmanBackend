from typing import List

from fastapi import FastAPI, Header
from fastapi.middleware.cors import CORSMiddleware
from tortoise.contrib.fastapi import register_tortoise

from models import Order_Pydantic, OrderIn_Pydantic, Orders


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


@app.get('/api/orders', response_model=List[Order_Pydantic])
async def get_orders(request_user_id: str = Header(None)):
    return await Order_Pydantic.from_queryset(
        Orders.filter(created_by=request_user_id)
    )


@app.post('/api/orders', response_model=Order_Pydantic)
async def create_order(order: OrderIn_Pydantic,
                      request_user_id: str = Header(None)):
    data = order.dict()
    data.update({'created_by': request_user_id})

    order_obj = await Orders.create(**data)
    return await Order_Pydantic.from_tortoise_orm(order_obj)


register_tortoise(
    app,
    db_url='sqlite://:memory:',
    modules={'models': ['models']},
    generate_schemas=True,
    add_exception_handlers=True,
)

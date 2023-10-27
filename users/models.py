from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from db import engine, meta

users = Table("users", meta, Column("id",Integer,primary_key=True),
    Column("email",String(255), nullable=False),
    Column("password",String(255),nullable=False ),          
    Column("Role",String(255),nullable=False),          
    Column("Banned",Integer,nullable=False),
    Column('user_type',String(255), nullable=False)          
)

meta.create_all(engine)
from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from db import engine, meta

users = Table("users", meta, 
    Column("id",Integer,primary_key=True),
    Column("username",String(255), nullable=False),
    Column("email",String(255), nullable=False),
    Column("address",String(255)),
    Column("state_province",String(255)),
    Column("city",String(255), nullable=False),
    Column("country",String(255), ),
    Column("zip_code",String(255)),
    Column("hashed_password",String(255),nullable=False ),              
    Column('user_type',String(255), nullable=False),
    Column("banned",Integer,nullable=False),
    # Column("profile_picture",String(255)),
              
)

meta.create_all(engine)
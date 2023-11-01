from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, Boolean
from db import engine, meta
from datastructures import UserInDbChk
from sqlalchemy.orm import declarative_base



users = Table("users", meta, 
    Column("id",Integer,primary_key=True),
    Column("username",String(255), unique=True, nullable=False),
    Column("email",String(255), nullable=False),
    Column("address",String(255)),
    Column("state_province",String(255)),
    Column("city",String(255), nullable=False),
    Column("country",String(255), ),
    Column("zip_code",String(255)),
    Column("hashed_password",String(255),nullable=False ),              
    Column('user_type',String(255), nullable=False),
    Column("banned",Integer,nullable=False),
    Column("profile_picture",String(255)),
              
)

Base = declarative_base()

class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True)
    text = Column(String(255))
    is_done = Column(Boolean, default=False)


Base.metadata.create_all(engine)

#meta.create_all(engine)
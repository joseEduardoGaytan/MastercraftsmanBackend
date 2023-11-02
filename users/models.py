from sqlalchemy import Table, Column, inspect
from sqlalchemy.sql.sqltypes import Integer, String, Boolean
from db import engine, meta
from datastructures import UserInDbChk
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"   

    id = Column(Integer, primary_key=True)
    username = Column(String(255), unique=True, nullable=False)
    email = Column(String(255), nullable=False)
    address = Column(String(255))
    state_province = Column(String(255))
    city = Column(String(255), nullable=False)
    country =Column(String(255))
    zip_code=Column(String(255))
    hashed_password = Column(String(255),nullable=False )
    user_type = Column(String(255), nullable=False)
    banned = Column(Integer,nullable=False)
    profile_picture =Column(String(255))


Base.metadata.create_all(engine)
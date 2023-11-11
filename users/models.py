#from sqlalchemy import Table, Column, inspect
#from sqlalchemy.sql.sqltypes import Integer, String, Boolean
#from db import engine, meta
#rom sqlalchemy.orm import declarative_base

#Base = declarative_base()

# class User(Base):
#     __tablename__ = "users"   

#     id = Column(Integer, primary_key=True)
#     username = Column(String(255), unique=True, nullable=False)
#     email = Column(String(255), nullable=False)
#     address = Column(String(255))
#     state_province = Column(String(255))
#     city = Column(String(255), nullable=False)
#     country =Column(String(255))
#     zip_code=Column(String(255))
#     hashed_password = Column(String(255),nullable=False )
#     user_type = Column(String(255), nullable=False)
#     banned = Column(Integer,nullable=False)
#     profile_picture =Column(String(255))


#Base.metadata.create_all(engine)

from tortoise.models import Model
from tortoise import fields
from tortoise.contrib.pydantic import pydantic_model_creator
from pydantic import BaseModel

class User(Model):
    class PydanticMeta:
        exclude = ('hashed_password')
    class Meta:
        table = "users"
    
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=255,unique=True)
    email = fields.CharField(max_length=255)
    address = fields.CharField(max_length=255)
    state_province = fields.CharField(max_length=255)
    city = fields.CharField(max_length=255)
    country = fields.CharField(max_length=255)
    zip_code = fields.CharField(max_length=255)
    hashed_password = fields.CharField(max_length=255)
    user_type = fields.CharField(max_length=255)
    banned = fields.IntField()
    profile_picture = fields.CharField(max_length=255)


User_Pydantic = pydantic_model_creator(User, name='User')
UserIn_Pydantic = pydantic_model_creator(User, name='UserIn', exclude_readonly=True)
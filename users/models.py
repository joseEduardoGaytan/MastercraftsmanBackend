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
    first_name = fields.CharField(max_length=255)
    last_name = fields.CharField(max_length=255)
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
from tortoise.models import Model
from tortoise import fields, Tortoise
from tortoise.contrib.pydantic import pydantic_model_creator
from pydantic import BaseModel

class TypeOfWork(Model):
    class Meta:
        table = 'typeofworks'

    def __str__(self):
        return self.name
    
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)
    typeofworks: fields.ReverseRelation["Contractor"]
    

class Contractor(Model):    
    class Meta:
        table = "contractors"
    
    def __str__(self):
        return f'{self.business_name}-{self.owner_name}'
    
    id = fields.IntField(pk=True)
    owner_name = fields.CharField(max_length=255)
    business_name = fields.CharField(max_length=255)
    certifications = fields.TextField()
    size_of_enterprice = fields.CharField(max_length=255)
    availability = fields.CharField(max_length=255)#change to enum
    rage_of_area = fields.JSONField() #investigate how to implement this
    state_province = fields.CharField(max_length=255)
    city = fields.CharField(max_length=255)
    country = fields.CharField(max_length=255)
    zip_code = fields.CharField(max_length=255)
    profile_picture = fields.CharField(max_length=255)    
    # tournament: fields.ForeignKeyRelation[Tournament] = fields.ForeignKeyField(
    #     "models.Tournament", related_name="events", description="The Tournament this happens in"
    # )

    type_of_work : fields.ForeignKeyRelation[TypeOfWork] = fields.ForeignKeyField('models.TypeOfWork', related_name='typeofworks')
    


Tortoise.init_models(["models"], "models")

Contractor_Pydantic = pydantic_model_creator(Contractor,name='Contractor')
ContractorIn_Pydantic = pydantic_model_creator(Contractor, name='ContractorIn', exclude_readonly=True)
TypeOfWork_Pydantic = pydantic_model_creator(TypeOfWork, name='TypeOfWork')
TypeOfWorkIn_Pydantic = pydantic_model_creator(TypeOfWork, name='TypeOfWorkIn')
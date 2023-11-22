from models import Contractor, Contractor_Pydantic, ContractorIn_Pydantic


async def get_all_contractors():      
    contractors_list = await Contractor_Pydantic.from_queryset(Contractor.all())    
    return contractors_list

async def get_contractor_by_id(contractor_id: int):    
    contractor_exists = await Contractor.get_or_none(id=contractor_id).exists()    
    if contractor_exists:        
        return await Contractor_Pydantic.from_queryset_single(Contractor.get(id=contractor_id))            
    return None

async def insert_contractor(data: dict):    
    contractor_obj = await Contractor.create(**data)    
    return await Contractor_Pydantic.from_tortoise_orm(contractor_obj)

async def update_contractor(contractor_id: int):
    contractor_exists = await Contractor.get_or_none(id=contractor_id).exists()
    if contractor_exists:                                           
        await contractor.filter(id=contractor_id).update(**data.dict(exclude_none=True,exclude_unset=True))        
        return await get_contractor_by_id(contractor_id)                     
    else:
        return None

async def delete_contractor(Contractor_id: int):
    contractor_exists = await contractor.get_or_none(id=contractor_id).exists()
    if not contractor_exists:                                                
        return False
    return await contractor.filter(id=contractor_id).delete()
    
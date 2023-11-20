from models import Contractor, Contractor_Pydantic, ContractorIn_Pydantic


async def get_all_contractors():
    contractors_list = await Contractor_Pydantic.from_queryset(Contractor.all())    
    return contractors_list
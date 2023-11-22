from pydantic import BaseModel
from typing import Any

class ContractorsForm(BaseModel):
    owner_name : str 
    business_name : str 
    certifications : str 
    size_of_enterprice : str 
    availability : str 
    rage_of_area : Any 
    state_province : str 
    city : str 
    country : str 
    zip_code : str 
    profile_picture : str
    typeofwork_id : int = None
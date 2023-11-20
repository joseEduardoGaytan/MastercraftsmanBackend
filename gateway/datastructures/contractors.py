from pydantic import BaseModel
from typing import Optional, Any

class ContractorsForm(BaseModel):
    #id : Optinal[int] 
    owner_name : str
    business_name : str
    certifications : str
    size_of_enterprice :str
    availability : str
    rage_of_area : str
    state_province : str
    city : str
    country : str
    zip_code : str
    profile_picture  : str
    type_of_work : int

class ContractorsResponse(BaseModel):
    id : Optional[int] = None
    owner_name : str
    business_name : str
    certifications : str
    size_of_enterprice :str
    availability : str
    rage_of_area : Any = None
    state_province : str
    city : str
    country : str
    zip_code : str
    profile_picture  : str
    type_of_work : Any = None
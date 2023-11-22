import requests, random
from test_users import API_URL,credentials_payload, get_token, get_authorization_token

response = get_token(credentials_payload)
auth_token = get_authorization_token(response.json())
    
# def get_token(payload):    
#     response = requests.post(API_URL+'/api/login',json=payload)
#     assert response.status_code == 201    
#     return response

#Test with a valid auth token get a list of contractors
def test_can_list_contractors():
    response_list_contractors = requests.get(API_URL+'/api/contractors',headers=auth_token)
    assert response_list_contractors.status_code == 200
    assert isinstance(response_list_contractors.json(),list)
    
#Tests can manage contractors
def test_can_create_update_delete_contractors():
    payload={'owner_name' :  f'a{random.randint(1,10000)}','business_name' : 'a', 'certifications' : 'a', 'size_of_enterprice' :'a','availability' : 'a','rage_of_area' : '{}','state_province' : 'a', 'city' : 'a', 'country' : 'a', 'zip_code' : 'a', 'profile_picture'  : 'a', 'typeofwork_id' : 1}
    
    response_contractor_create = requests.post(API_URL+'/api/contractors',headers=auth_token, json=payload)    
    assert response_contractor_create.status_code == 201
    
    
    pass
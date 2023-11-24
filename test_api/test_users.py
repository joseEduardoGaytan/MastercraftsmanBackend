import requests
import jwt
import random

API_URL = 'http://localhost:8001'
SECRET = 'e0e5f53b239df3dc39517c34ae0a1c09d1f5d181dfac1578d379a4a5ee3e0ef5'
ALGORITHM = 'HS256'
credentials_payload = {"username":"admin","password":"a"}

#Get token with valid credentials
def get_token(payload):    
    response = requests.post(API_URL+"/api/login",json=payload)
    assert response.status_code == 201    
    return response

#Encode token response with jwt
def get_authorization_token(token):
    token_encoded = jwt.encode(token,SECRET,ALGORITHM)
    return {'Authorization': token_encoded}
    
#Test api login with valid credentials
def test_can_login():         
    response = requests.post(API_URL+ "/api/login" ,json=credentials_payload)    
    assert response.status_code == 201

#Test api login with invalid credentials error
def test_invalid_credentials():
    invalid_credentials = {"username":"other","password":"abc"}
    response = requests.post(API_URL+ "/api/login" ,json=invalid_credentials)
    assert response.status_code == 401
    assert response.json() == {'detail': 'Invalid credentials'}

#Test with a valid auth token get a list of users
def test_can_list_users():    
    response_token = get_token(credentials_payload)    
    auth_token = get_authorization_token(response_token.json())       
    response_list_users = requests.get(API_URL+'/api/users',headers=auth_token)
    assert response_list_users.status_code == 200    
    assert isinstance(response_list_users.json(),list)

#Tests can manage users
def test_can_create_update_delete_users():

    response_token = get_token(credentials_payload)    
    auth_token = get_authorization_token(response_token.json())

    #create user
    payload={'username': f'admin{random.randint(1,10000)}', 'email': 'admin@master.com', 'address': '5th ave # 21', 'first_name': 'user', 'last_name': 'master craft', 'state_province': 'zacatecas', 'city': 'zacatecas', 'country': 'mexico', 'zip_code': '9802', 'user_type': 'default', 'banned': 0, 'profile_picture': '', 'password':"ab"} 
    response_user_create = requests.post(API_URL+'/api/users',headers=auth_token, json=payload)        
    assert response_user_create.status_code == 201    
        
    #get user with user_id create before
    user_data =  response_user_create.json()    
    user_id = user_data['id']
    response_user_get = requests.get(API_URL+f'/api/users/{user_id}',headers=auth_token)
    assert response_user_get.status_code == 200
    assert user_data == response_user_get.json()
    
    #edit user
    user_data['banned']=1
    response_user_update = requests.put(API_URL+f'/api/users/{user_id}',headers=auth_token, json=user_data)
    assert response_user_update.status_code == 200
    assert response_user_update.json()['banned'] == 1

    #delete user
    response_user_delete = requests.delete(API_URL+f'/api/users/{user_id}',headers=auth_token)
    assert response_user_delete.status_code == 200
    assert response_user_delete.json() == {'message': 'user has been deleted'}

#validate user not found
def test_user_not_exis():
    response_token = get_token(credentials_payload)    
    auth_token = get_authorization_token(response_token.json())
    user_id = 99999999
    response_user_search = requests.get(API_URL+f'/api/users/{user_id}',headers=auth_token)
    response_user_search.status_code == 404

#validate user not found when request a delete
def test_user_delete_error():
    response_token = get_token(credentials_payload)    
    auth_token = get_authorization_token(response_token.json())
    user_id = 9999
    response_user_delete = requests.delete(API_URL+f'/api/users/{user_id}',headers=auth_token)
    response_user_delete.status_code == 404
    assert response_user_delete.json() == {'detail': 'User cannot be deleted'}


    
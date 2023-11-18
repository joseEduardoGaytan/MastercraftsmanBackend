import requests

API_URL = 'http://localhost:8001'

#Test api login with valid credentials
def test_can_login():
    payload = {"username":"admin","password":"a"}
    response = requests.post(API_URL+ "/api/login" ,json=payload)
    assert response.status_code == 201
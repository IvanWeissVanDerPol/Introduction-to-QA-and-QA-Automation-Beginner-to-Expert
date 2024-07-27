import pytest
import requests
from assertpy import assert_that

BASE_URL = "https://reqres.in/api"

def create_user(data):
    response = requests.post(f"{BASE_URL}/users", json=data)
    assert_that(response.status_code).is_equal_to(201)
    return response.json()

def get_users(page):
    response = requests.get(f"{BASE_URL}/users", params={"page": page})
    assert_that(response.status_code).is_equal_to(200)
    return response.json()

def update_user(user_id, data):
    response = requests.put(f"{BASE_URL}/users/{user_id}", json=data)
    assert_that(response.status_code).is_equal_to(200)
    return response.json()

def delete_user(user_id):
    response = requests.delete(f"{BASE_URL}/users/{user_id}")
    assert_that(response.status_code).is_equal_to(204)

@pytest.mark.run(order=1)
def test_create_user():
    data = {"name": "John", "job": "developer"}
    json_data = create_user(data)

    assert_that(json_data).contains_key('id').contains_key('createdAt')
    assert_that(json_data['name']).is_equal_to(data['name'])
    assert_that(json_data['job']).is_equal_to(data['job'])

    global user_id
    user_id = json_data['id']

@pytest.mark.run(order=2)
def test_get_users():
    json_data = get_users(2)
    
    assert_that(json_data['page']).is_equal_to(2)
    assert_that(json_data['data']).is_not_empty()
    
    for user in json_data['data']:
        assert_that(user).contains_key('id').contains_key('email')
        assert_that(user['email']).matches(r'^[\w\.-]+@[\w\.-]+\.\w+$')

@pytest.mark.run(order=3)
def test_update_user():
    data = {"name": "John", "job": "manager"}
    json_data = update_user(user_id, data)

    assert_that(json_data).contains_entry({'name': 'John'}).contains_entry({'job': 'manager'}).contains_key('updatedAt')
    assert_that(json_data['updatedAt']).is_not_empty()

@pytest.mark.run(order=4)
def test_delete_user():
    delete_user(user_id)

if __name__ == "__main__":
    pytest.main()

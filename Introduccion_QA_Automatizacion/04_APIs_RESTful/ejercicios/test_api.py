import pytest
import requests
from assertpy import assert_that

BASE_URL = "https://reqres.in/api"

@pytest.mark.run(order=1)
def test_create_user():
    data = {"name": "John", "job": "developer"}
    response = requests.post(f"{BASE_URL}/users", json=data)
    json_data = response.json()

    assert_that(response.status_code).is_equal_to(201)
    assert_that(json_data).contains_key('id').contains_key('createdAt')
    global user_id
    user_id = json_data['id']

@pytest.mark.run(order=2)
def test_get_users():
    response = requests.get(f"{BASE_URL}/users?page=2")
    json_data = response.json()
    
    assert_that(response.status_code).is_equal_to(200)
    assert_that(json_data['data']).is_not_empty()
    assert_that(json_data['data'][0]).contains_key('id').contains_key('email')

@pytest.mark.run(order=3)
def test_update_user():
    data = {"name": "John", "job": "manager"}
    response = requests.put(f"{BASE_URL}/users/{user_id}", json=data)
    json_data = response.json()

    assert_that(response.status_code).is_equal_to(200)
    assert_that(json_data).contains_entry({'name': 'John'}).contains_entry({'job': 'manager'}).contains_key('updatedAt')

@pytest.mark.run(order=4)
def test_delete_user():
    response = requests.delete(f"{BASE_URL}/users/{user_id}")
    assert_that(response.status_code).is_equal_to(204)

if __name__ == "__main__":
    pytest.main()

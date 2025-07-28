from fastapi import Response
from fastapi.testclient import TestClient

BASE_URL = "/api/v1"

def test_get_all_clients(client: TestClient):
    result: Response = client.get(f"{BASE_URL}/clients")
    assert result.status_code == 200
    data = result.json()
    assert isinstance(data, list)
    assert len(data) > 0
    
def test_get_client_by_id(client: TestClient):
    pass

def test_create_client(client: TestClient):
    new_client = {
        "firstname": "john",
        "lastname": "doe",
        "address_line_1": "123 Main St",
        "newsletter": 1
    }
    result: Response = client.post(f"{BASE_URL}/clients", json=new_client)
    assert result.status_code == 201
    created_client: dict = result.json()
    assert created_client["firstname"] == "John"
    assert created_client["lastname"] == "DOE"
    assert created_client["address_line_1"] == "123 Main St"
    assert created_client["newsletter"] == True

def test_patch_client(client: TestClient):
    pass

def test_delete_client(client: TestClient):
    pass
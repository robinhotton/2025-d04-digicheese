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
    pass

def test_patch_client(client: TestClient):
    pass

def test_delete_client(client: TestClient):
    pass
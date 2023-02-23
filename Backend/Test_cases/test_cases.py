from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

data = {
    "ngoName": "string",
    "contactPersonName": "string",
    "contactPersonEmail": "user@example.com",
    "contactPersonPhone": "7578061886",
    "contactPersonPassword": "string",
    "location": "string",
    "pincode": "784115"
}


def test_create_ngo():
    response = client.post("/create_ngo", json=data)
    assert response.status_code == 200


def test_create_ngo_with_wrong_phone_number():
    response = client.post("/create_ngo", json={
        "ngoName": "string",
        "contactPersonName": "string",
        "contactPersonEmail": "user@example.com",
        "contactPersonPhone": "757806188",
        "contactPersonPassword": "string",
        "location": "string",
        "pincode": "784115"
    })
    assert response.status_code == 200


def test_create_ngo_with_wrong_url():
    response = client.post("/create", json={
        "ngoName": "string",
        "contactPersonName": "string",
        "contactPersonEmail": "user@example.com",
        "contactPersonPhone": "757806188",
        "contactPersonPassword": "string",
        "location": "string",
        "pincode": "784115"
    })
    assert response.status_code == 200


def test_getNgos():
    response = client.get("/getNgos")
    assert response.status_code == 200


def test_getNgo():
    response = client.get("/get_ngo/626bccb9697a12204fb22ea3")
    assert response.status_code == 200


def test_updateNgo():
    response = client.put("/ngos/0", json={
        "ngoName": "test",
        "contactPersonName": "string",
        "contactPersonEmail": "user@example.com",
        "contactPersonPhone": "7578061886",
        "contactPersonPassword": "string",
        "location": "string",
        "pincode": "784115"})
    assert response.status_code == 200


def test_Wrong_updateNgo():
    response = client.put("/ngos/0", json={
        "ngoName": "test",
        "contactPersonName": "string",
        "contactPersonEmail": "user@example.com",
        "contactPersonPhone": "7578061886",
        "contactPersonPassword": "string",
        "location": "string",
        "pincode": "7841156"})
    assert response.status_code == 200


def test_deleteNgo():
    response = client.delete("/delete_ngo/626bccb9697a12204fb22ea3")
    assert response.status_code == 200

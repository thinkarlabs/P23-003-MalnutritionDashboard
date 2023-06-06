from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

data = {
    "contactPersonName": "string",
    "contactPersonPhone": "string",
    "contactPersonPassword": "string",
    "location_coordinates": "string",
    "location": "string"
}


# Positive Test Cases

# Test case: Add Aanganwadi
def test_add_aanganwadi():
    response = client.post("/api/addAanganwadi", json=data)
    assert response.status_code == 200
    result = response.json()
    assert result["status"] == "ok"
    assert "data" in result


# Test case: Get All Aanganwadis
def test_get_aanganwadis():
    response = client.get("api/getAanganwadis")
    assert response.status_code == 200
    result = response.json()
    assert result["status"] == "ok"
    assert "data" in result


# Test case: Get Aanganwadi by ID
def test_get_aanganwadi():
    # Add an Aanganwadi first to get its ID
    add_response = client.post("/api/addAanganwadi", json=data)
    added_data = add_response.json()["data"]
    aanganwadi_id = added_data[0]["_id"]
    response = client.get("/api/{aanganwadi_id}/get_aanganwadi")
    assert response.status_code == 200
    result = response.json()
    assert result["status"] == "ok"
    assert "data" in result


# Test case: Update Aanganwadi
def test_update_aanganwadi():
    # Add an Aanganwadi first to update it later
    add_response = client.post("/api/addAanganwadi", json=data)
    added_data = add_response.json()["data"]
    aanganwadi_id = added_data[0]["_id"]

    updated_data = data.copy()
    updated_data["contactPersonName"] = "Updated Name"
    response = client.put(f"/api/updateAanganwadi/{aanganwadi_id}", json=updated_data)
    assert response.status_code == 200
    result = response.json()
    assert result["status"] == "ok"
    assert "data" in result


# Test case: Delete Aanganwadi
def test_delete_aanganwadi():
    # Add an Aanganwadi first to delete it later
    add_response = client.post("/api/addAanganwadi", json=data)
    added_data = add_response.json()["data"]
    aanganwadi_id = added_data[0]["_id"]
    response = client.delete(f"/api/delete_aanganwadi/{aanganwadi_id}")
    assert response.status_code == 200
    result = response.json()
    assert result["status"] == "ok"
    assert "data" in result


# Negative Test Cases

# Test case: Add Aanganwadi with Invalid Data
def test_add_aanganwadi_invalid_data():
    invalid_data = data.copy()
    invalid_data["contactPersonPhone"] = "12345"  # Invalid phone number
    response = client.post("/api/addAanganwadi", json=invalid_data)
    assert response.status_code == 400
    result = response.json()
    assert "detail" in result


# Test case: Get Aanganwadi with Invalid ID
def test_get_aanganwadi_invalid_id():
    invalid_id = "invalid_id"
    response = client.get(f"/api/{invalid_id}/get_aanganwadi")
    assert response.status_code == 400
    result = response.json()
    assert "detail" in result


# Test case: Update Aanganwadi with Invalid ID
def test_update_aanganwadi_invalid_id():
    invalid_id = "invalid_id"
    response = client.put(f"/api/updateAanganwadi/{invalid_id}", json=data)
    assert response.status_code == 400
    result = response.json()
    assert "detail" in result


# Test case: Delete Aanganwadi with Invalid ID
def test_delete_aanganwadi_invalid_id():
    invalid_id = "invalid_id"
    response = client.delete(f"/api/delete_aanganwadi/{invalid_id}")
    assert response.status_code == 400
    result = response.json()
    assert "detail" in result


# Test case: Get Non-existent Aanganwadi
def test_get_non_existent_aanganwadi():
    non_existent_id = "non_existent_id"
    response = client.get(f"/api/{non_existent_id}/get_aanganwadi")
    assert response.status_code == 404
    result = response.json()
    assert "detail" in result

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


# positive sceanrios

# Add Child
def test_add_child_valid_input():
    # Prepare valid input data
    valid_input = {
        "childName": "John",
        "motherName": "Jane",
        "child_age": "5",
        "gender": "Male",
        "isActive": True
    }
    # Send a POST request to add a child
    response = client.post("/api/add_child", json=valid_input)
    # Assert the response
    assert response.status_code == 200
    assert response.json()["status"] == "ok"
    assert "data" in response.json()


#  Get Childs
def test_get_childs_existing_records():
    # Send a GET request to retrieve all child records
    response = client.get("/api/get_childs")

    # Assert the response
    assert response.status_code == 200
    assert response.json()["status"] == "ok"
    assert "data" in response.json()


# Get Child by ID
def test_get_child_valid_id():
    # Provide a valid child ID
    valid_child_id = "valid_id_here"

    # Send a GET request to retrieve the specific child by ID
    response = client.get(f"/api/{valid_child_id}/get_child")

    # Assert the response
    assert response.status_code == 200
    assert response.json()["status"] == "ok"
    assert "data" in response.json()


# Update Child
def test_update_child_valid_input():
    # Provide a valid child ID
    valid_child_id = "valid_id_here"
    # Prepare valid input data for updating child
    valid_input = {
        "childName": "Updated John",
        "motherName": "Updated Jane",
        "child_age": "6",
        "gender": "Male",
        "isActive": True
    }
    # Send a PUT request to update the child record
    response = client.put(f"/api/updatechild/{valid_child_id}", json=valid_input)
    # Assert the response
    assert response.status_code == 200
    assert response.json()["status"] == "ok"
    assert "data" in response.json()


# Delete Child
def test_delete_child_valid_id():
    # Provide a valid child ID
    valid_child_id = "valid_id_here"
    # Send a DELETE request to delete the child record
    response = client.delete(f"/api/deletechild?id={valid_child_id}")
    # Assert the response
    assert response.status_code == 200
    assert response.json()["status"] == "ok"
    assert "data" in response.json()


# Negative Test Cases

# Add Child
def test_add_child_invalid_input():
    # Prepare invalid input data with missing required fields
    invalid_input = {
        "childName": "John",
        "gender": "Male"
    }
    # Send a POST request to add a child with invalid input
    response = client.post("/api/add_child", json=invalid_input)
    # Assert the response
    assert response.status_code == 422


# Get Child by ID
def test_get_child_invalid_id():
    # Provide an invalid child ID
    invalid_child_id = "invalid_id_here"
    # Send a GET request with an invalid child ID
    response = client.get(f"/api/{invalid_child_id}/get_child")
    # Assert the response
    assert response.status_code == 404


# Update Child
def test_update_child_invalid_input():
    # Provide an invalid child ID
    invalid_child_id = "invalid_id_here"

    # Prepare invalid input data for updating child
    invalid_input = {
        "childName": "Updated John",
        "gender": "Male"
    }
    # Send a PUT request with invalid input
    response = client.put(f"/api/updatechild/{invalid_child_id}", json=invalid_input)
    # Assert the response
    assert response.status_code == 422


# Delete Child
def test_delete_child_invalid_id():
    # Provide an invalid child ID
    invalid_child_id = "invalid_id_here"
    # Send a DELETE request with an invalid child ID
    response = client.delete(f"/api/deletechild?id={invalid_child_id}")
    # Assert the response
    assert response.status_code == 404

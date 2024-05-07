from fastapi.testclient import TestClient
from main import app 

client = TestClient(app)

# Utility function to authenticate and get a token
def get_user_token():
    response = client.post("/login", data={"username": "test@test.com", "password": "test12"})
    return response.json()["access_token"]

# Test getting all todos
def test_get_todos():
    token = get_user_token()
    response = client.get("/todos", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200

# Test creating a new todo
def test_create_todo():
    token = get_user_token()
    todo_data = {"title": "New Task", "description": "Complete this task", "completed": False}
    response = client.post("/todos", json=todo_data, headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200
    assert "id" in response.json()

# Test handling of non-existent todo
def test_delete_nonexistent_todo():
    token = get_user_token()
    response = client.delete("/todos/nonexistent_todo_id", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 404

def test_get_update_delete_todo():
    token = get_user_token()
    # Create a new todo
    todo_data = {"title": "Temporary Task", "description": "Delete this later", "completed": False}
    create_response = client.post("/todos", json=todo_data, headers={"Authorization": f"Bearer {token}"})
    assert create_response.status_code == 200
    todo_id = create_response.json()["id"]

    # Test retrieving the specific todo
    get_response = client.get(f"/todos/{todo_id}", headers={"Authorization": f"Bearer {token}"})
    assert get_response.status_code == 200

    # Test updating the todo
    updated_todo_data = {"title": "Updated Task", "description": "Updated description", "completed": True}
    update_response = client.put(f"/todos/{todo_id}", json=updated_todo_data, headers={"Authorization": f"Bearer {token}"})
    assert update_response.status_code == 200

    # Test deleting the todo
    delete_response = client.delete(f"/todos/{todo_id}", headers={"Authorization": f"Bearer {token}"})
    assert delete_response.status_code == 200
from fastapi.testclient import TestClient
from main import app  # Import your FastAPI app

client = TestClient(app)

def test_register_user():
    response = client.post("/register", json={"email": "test6@test.com", "password": "testpas6"})
    assert response.status_code == 200
    assert response.json() == {"message": "User registered successfully"}

def test_login_user():
    # Ensure the user is registered first
    client.post("/register", json={"email": "yvann075@gmail.com", "password": "test12"})
    response = client.post("/login", data={"username": "test@example.com", "password": "testpassword"})
    assert response.status_code == 200
    assert "access_token" in response.json()
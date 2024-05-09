from fastapi.testclient import TestClient
import random
import string
from main import app  # Import your FastAPI app

client = TestClient(app)

# response = client.post("/register", json={"email": "test6@test.com", "password": "testpas6"})

def test_register_user():
    # Generate a random email
    email = f"test{random.randint(1, 10000)}@pourlascience.com"
    # Generate a random password
    password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    
    response = client.post("/register", json={"email": email, "password": password})
    assert response.status_code == 200
    assert response.json() == {"message": "User registered successfully"}

def test_login_user():
    # Ensure the user is registered first
    client.post("/register", json={"email": "yvann075@gmail.com", "password": "test12"})
    response = client.post("/login", data={"username": "test@example.com", "password": "testpassword"})
    assert response.status_code == 200
    assert "access_token" in response.json()
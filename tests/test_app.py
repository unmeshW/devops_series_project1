import sys
import os
import pytest

# Add the root project folder to sys.path so 'app' can be imported
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app

# Enable testing mode for Flask
app.testing = True
client = app.test_client()

def test_home():
    """Test the home route '/'"""
    response = client.get('/')
    assert response.status_code == 200
    data = response.get_json()
    assert data["message"] == "Hello all, Welcome to my WebApp..!!!"

def test_health_check():
    """Test the health check route '/health'"""
    response = client.get('/health')
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "All Healthy"
    assert "timestamp" in data

def test_get_users():
    """Test the users API route '/api/users'"""
    response = client.get('/api/users')
    assert response.status_code == 200
    data = response.get_json()
    assert data[0]["name"] == "Unmesh"
    assert data[0]["role"] == "Cloud support engineer"
    assert data[1]["name"] == "Tony"
    assert data[1]["role"] == "Site reliability engineer"

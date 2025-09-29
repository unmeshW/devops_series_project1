import pytest
from app import app

# Enable testing mode for Flask
app.testing = True
client = app.test_client()

def test_home_page():
    """Test the home page '/'"""
    response = client.get('/')
    assert response.status_code == 200
    assert b"Welcome to My WebApp" in response.data
    assert b"Check" in response.data  # Checking presence of links

def test_health_page():
    """Test the health page '/health'"""
    response = client.get('/health')
    assert response.status_code == 200
    assert b"Status: All Healthy" in response.data
    assert b"Timestamp (UTC)" in response.data

def test_users_page():
    """Test the users page '/users'"""
    response = client.get('/users')
    assert response.status_code == 200
    # Check for user names in HTML table
    assert b"Unmesh" in response.data
    assert b"Cloud Support Engineer" in response.data
    assert b"Tony" in response.data
    assert b"Site Reliability Engineer" in response.data

def test_invalid_route():
    """Test a route that does not exist"""
    response = client.get('/invalid')
    assert response.status_code == 404

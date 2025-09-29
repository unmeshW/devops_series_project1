import sys
import os
import pytest

# Add project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app

# Enable testing mode
app.testing = True
client = app.test_client()

def test_home():
    """Test the home route '/'"""
    response = client.get('/')
    assert response.status_code == 200
    html = response.data.decode('utf-8')
    assert "Welcome to my WebApp" in html  # check if expected text exists

def test_health_check():
    """Test the health check route '/health'"""
    response = client.get('/health')
    assert response.status_code == 200
    html = response.data.decode('utf-8')
    assert "All Healthy" in html

def test_get_users():
    """Test the users API route '/api/users'"""
    response = client.get('/api/users')
    assert response.status_code == 200
    html = response.data.decode('utf-8')
    # Make sure expected user names exist in the output
    assert "Unmesh" in html
    assert "Cloud support engineer" in html
    assert "Tony" in html
    assert "Site reliability engineer" in html

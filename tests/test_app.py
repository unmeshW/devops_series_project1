import sys
import os
import pytest

# Ensure parent directory is in path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import app

app.testing = True
client = app.test_client()

def test_home():
    """Test the home route '/'"""
    response = client.get('/')
    assert response.status_code == 200
    html = response.data.decode('utf-8')
    assert "Hello all, Welcome to my WebApp" in html

def test_health_check():
    """Test the health check route '/health'"""
    response = client.get('/health')
    assert response.status_code == 200
    html = response.data.decode('utf-8')
    assert "All Healthy" in html

def test_users():
    """Test the users route '/users'"""
    response = client.get('/users')
    assert response.status_code == 200
    html = response.data.decode('utf-8')
    assert "Unmesh" in html
    assert "Cloud support engineer" in html
    assert "Tony" in html
    assert "Site reliability engineer" in html

from app import app
import unittest, requests

def test_page_response():
    response = requests.get("https://www.google.com")
    assert response.status_code == 200 

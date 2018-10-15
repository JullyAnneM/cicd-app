import unittest, requests

def test_img_api():
    response = requests.get("http://placekitten.com/510/210")
    assert response.status_code == 200 

def test_fact_api():
    responde = requests.get("https://catfact.ninja/fact")
    assert response.status_code == 200

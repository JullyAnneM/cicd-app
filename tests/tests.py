import unittest, requests

def test_img_api():
    resp = requests.get("http://placekitten.com/510/210")
    assert resp.status_code == 200 

def test_fact_api():
    resp = requests.get("https://catfact.ninja/fact")
    assert resp.status_code == 200

from fastapi import FastAPI, applications
from fastapi.testclient import TestClient
import uvicorn

from src.main import app




client = TestClient(app)



def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "This is a GET call, checking with Rahul Taneja Koppr"}

def test_put_call():
    response = client.put("/")
    assert response.status_code == 200
    assert response.json() == {"message": "This is a PUT call"}



def test_post_call():
    response = client.post("/")
    assert response.status_code == 200
    assert response.json() == {"message": "This is a POST call"}



def test_delete_call():
    response = client.delete("/")
    assert response.status_code == 200
    assert response.json() == {"message": "This is a DELETE call"}
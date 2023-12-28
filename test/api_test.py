from fastapi.testclient import TestClient
from server.app import app
from helper import predict_test

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
            "description": "Welcome to the Weather2Watt API! This API predicts solar power efficiency using metereological data"
        }


def test_predict():
    response = predict_test(client, "/api/predict/")
    assert response["status_code"] == 200


from locust import HttpUser, task, between
from helper import predict_test


class PerformanceTests(HttpUser):
    wait_time = between(2, 5)

    @task(1)
    def test_fastapi(self):
        response = self.client.get("/")
        print(response.json())

    @task(2)
    def test_catboost_predict(self):
        result = predict_test(self.client, "/api/predict/")
        print("result", result)

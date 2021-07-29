import json
from locust import HttpUser, task
import test

class WebsiteUser(HttpUser):
    @task
    def myTest(self):
        response = self.client.post(
            "/", headers=test.headers, data=json.dumps({"data": [test.data]}))
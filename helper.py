from server.test_samples import test_sample_points
import json
from server.schema import PredictionInput
import random


def predict_test(client, api_url):
    sample = random.choice(test_sample_points)
    res = client.post(api_url,
                      data=json.dumps(sample))

    return res.json()
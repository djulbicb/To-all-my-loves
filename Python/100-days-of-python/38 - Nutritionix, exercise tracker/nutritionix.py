import json
import os
import requests

class Nutritionix:
    NUT_ID = os.environ.get("nutritionix_id")
    NUT_KEY = os.environ.get("nutritionix_key")
    NUT_URL = "https://trackapi.nutritionix.com/v2/natural/exercise"

    headers = {
        "x-app-id": NUT_ID,
        "x-app-key": NUT_KEY,
        "Content-Type": "application/json"
    }

    def process(self, user_input:str) -> json.JSONDecoder:
        body = {
            "query": user_input,
            "gender": "male",
            "weight_kg": 117,
            "height_cm": 190,
            "age": 32
        }

        return requests.post(url=self.NUT_URL, json=body, headers=self.headers).json()


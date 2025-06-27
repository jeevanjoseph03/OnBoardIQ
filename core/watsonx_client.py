import os
import requests
from dotenv import load_dotenv

load_dotenv()

class WatsonXClient:
    def __init__(self):
        self.api_key = os.getenv("IBM_API_KEY")
        self.project_id = os.getenv("PROJECT_ID")
        self.model_id = os.getenv("MODEL_ID")
        self.endpoint = os.getenv("ENDPOINT")
        self.access_token = self.get_access_token()

    def get_access_token(self):
        url = "https://iam.cloud.ibm.com/identity/token"
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        data = f"grant_type=urn:ibm:params:oauth:grant-type:apikey&apikey={self.api_key}"

        response = requests.post(url, headers=headers, data=data)
        if response.status_code == 200:
            return response.json()["access_token"]
        else:
            raise Exception(f"Failed to fetch access token: {response.json()}")

    def generate(self, prompt):
        url = f"{self.endpoint}/ml/v1/text/generation?version=2024-05-01"
        headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json"
        }
        payload = {
            "model_id": self.model_id,
            "project_id": self.project_id,
            "input": prompt,
            "parameters": {
                "decoding_method": "greedy",
                "max_new_tokens": 512
            }
        }

        response = requests.post(url, headers=headers, json=payload)

        if response.status_code == 200:
            return response.json()["results"][0]["generated_text"]
        else:
            print("API Error:", response.json())
            return None

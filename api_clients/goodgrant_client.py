# api_clients/goodgrant_client.py
import requests
from config import GOODGRANT_API_KEY

def call_goodgrant_api(endpoint, params=None):
    url = f"https://api.goodgrant.io/{endpoint}"
    headers = {
        "Authorization": f"Bearer {GOODGRANT_API_KEY}",
        "Content-Type": "application/json"
    }
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()


# api_clients/togetherai_client.py
import requests
from config import TOGETHERAI_API_KEY

def call_togetherai(prompt, model="llama-7b", temperature=0.7):
    url = "https://api.together.ai/v1/completions"
    headers = {
        "Authorization": f"Bearer {TOGETHERAI_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": model,
        "prompt": prompt,
        "temperature": temperature
    }
    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()  # Check for HTTP errors
    return response.json()


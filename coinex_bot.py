import requests
import hmac
import hashlib
import time
import json
from config import API_KEY, SECRET_KEY

BASE_URL = "https://api.coinex.com/v1"

def sign(params):
    param_str = '&'.join([f"{k}={params[k]}" for k in sorted(params)])
    return hmac.new(SECRET_KEY.encode(), param_str.encode(), hashlib.sha256).hexdigest()

def get_account_info():
    uri = "/balance/info"
    params = {
        "access_id": API_KEY,
        "tonce": int(time.time() * 1000),
    }
    signed = sign(params)
    headers = {
        "Authorization": signed,
        "Content-Type": "application/json"
    }
    response = requests.get(BASE_URL + uri, headers=headers, params=params)
    return response.json()

if __name__ == "__main__":
    result = get_account_info()
    print("📊 Account Info:")
    print(json.dumps(result, indent=2))

# main.py
import requests
import time
import hmac
import hashlib
from config import API_KEY, SECRET_KEY

BASE_URL = "https://api.coinex.com/v1"

def make_signature(params, secret_key):
    sorted_params = sorted(params.items())
    encoded = "&".join([f"{k}={v}" for k, v in sorted_params])
    return hmac.new(secret_key.encode(), encoded.encode(), hashlib.sha256).hexdigest()

def get_account_info():
    uri = "/balance/info"
    params = {
        "access_id": API_KEY,
        "tonce": int(time.time() * 1000)
    }
    sign = make_signature(params, SECRET_KEY)
    headers = {
        "Authorization": sign
    }

    response = requests.get(BASE_URL + uri, headers=headers, params=params)
    return response.json()

if __name__ == "__main__":
    print("ربات شروع شد...")
    info = get_account_info()
    print("اطلاعات حساب:", info)

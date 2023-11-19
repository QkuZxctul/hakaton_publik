import hmac
from time import time
import hashlib

def get_signature(api_secret_key, api_common_key):
    timestamp = str(round(time()))
    payload = f'timestamp={timestamp}&api_key={api_common_key}'
    sign = hmac.new(api_secret_key.encode("utf-8"), payload.encode("utf-8"), hashlib.sha256).hexdigest()
    final = {
        'signature': sign,
        'timestamp': timestamp,
        'api_common_key': api_common_key
    }
    return final

if __name__ == '__main__':
    api_secret = 'LFIHOSIUV987tf78a6tg8e65rg87es65g87es6ybOUYG876vf968rvgesohvu'
    api_key = 'kjhvfkuvYTFCY8748754vUGIUTYFVoupoan'
    data = get_signature(api_secret, api_key)

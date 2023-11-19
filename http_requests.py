import httpx
import asyncio
from random import randint
import datetime
from server_database.keys import *

async def post_http_request(url_request, data_request):
    async with httpx.AsyncClient() as client:
        response = await client.post(url=url_request, json=data_request, headers={"Content-Type": "application/json"})
        return response

async def get_http_request(url_request, data_request):
    async with httpx.AsyncClient() as client:
        response = await client.get(url=url_request, params=data_request)
        return response

if __name__ == '__main__':
    id_pallet = randint(1, 10**5)
    api_secret = 'LFIHOSIUV987tf78a6tg8e65rg87es65g87es6ybOUYG876vf968rvgesohvu'
    api_key = 'kjhvfkuvYTFCY8748754vUGIUTYFVoupoan'
    signature = (get_signature(api_secret, api_key))
    print(signature)

    r1 = asyncio.run(post_http_request('http://127.0.0.1:8001/production',{
        'id_pallet': id_pallet,
        'product_name': 'aasddas',
        'product_batch': '1221',
        'thing_quantity': 12,
        'data_of_manufacture': '2023-11-18',
        'expiration_date': '2023-12-18',
        'api_common_key': signature.get('api_common_key'),
        'signature': signature.get('signature'),
        'timestamp': signature.get('timestamp')
    }))
    r2 = asyncio.run(get_http_request('http://127.0.0.1:8001/one_pallet',{
        'id_pallet': id_pallet,
        'product_name': 'aasddas',
        'product_batch': '1221',
        'thing_quantity': 12,
        'data_of_manufacture': '2023-11-18',
        'expiration_date': '2023-12-18',
        'api_common_key': signature.get('api_common_key'),
        'signature': signature.get('signature'),
        'timestamp': signature.get('timestamp')
    }))
    r3 = asyncio.run(post_http_request('http://127.0.0.1:8001/change_pallet_status',{
        'id_pallet': id_pallet,
        'product_name': 'aasddas',
        'product_batch': '1221',
        'thing_quantity': 12,
        'data_of_manufacture': '2023-11-18',
        'expiration_date': '2023-12-18',
        'api_common_key': signature.get('api_common_key'),
        'signature': signature.get('signature'),
        'timestamp': signature.get('timestamp')
    }))
    r4 = asyncio.run(get_http_request('http://127.0.0.1:8001/information', {
        'api_common_key': signature.get('api_common_key'),
        'signature': signature.get('signature'),
        'timestamp': signature.get('timestamp')
    }))

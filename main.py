from fastapi import FastAPI
from pydantic import BaseModel
from server_handler import PaletSql
import hmac
import hashlib

palletInDb = PaletSql()
app = FastAPI()

class QrCode(BaseModel):
  id_pallet: int
  product_name: str
  product_batch: str
  thing_quantity: int
  data_of_manufacture: str
  expiration_date: str
  timestamp: str
  api_common_key: str
  signature: str

def check_signature(data):
  timestamp = data.get('timestamp')
  api_common_key = data.get('api_key')
  signature = data.get('signature')
  api_secret_key = palletInDb.get_secret_key(api_key=api_common_key).api_secret

  if not api_secret_key:
    return False
  payload = f'timestamp={timestamp}&api_key={api_common_key}'
  sign = hmac.new(api_secret_key.encode("utf-8"), payload.encode("utf-8"), hashlib.sha256).hexdigest()
  if signature != sign:
    return False
  return True

@app.get("/information")
async def information(signature: str, timestamp: str, api_common_key: str):
  sign_check_data = {
    'signature': signature,
    'timestamp': timestamp,
    'api_key': api_common_key
  }
  signature_check = check_signature(sign_check_data)
  if signature_check:
    response = palletInDb.information()
    return response
  else:
    return {'message': 'invalid_signature'}


@app.get('/one_pallet')
async def one_pallet(signature: str, timestamp: str, api_common_key: str, id_pallet: str):
  sign_check_data = {
    'signature': signature,
    'timestamp': timestamp,
    'api_key': api_common_key
  }
  signature_check = check_signature(sign_check_data)
  if signature_check:
    try:
      response = palletInDb.one_pallet(id_pallet)
      return response
    except Exception:
      return {'message': 'there is no pallet with this id'}
  else:
    return {'message': 'invalid signature'}


@app.post('/production')
async def production(parameters: QrCode):
  sign_check_data = {
      'signature': parameters.signature,
      'timestamp': parameters.timestamp,
      'api_key': parameters.api_common_key
    }
  signature_check = check_signature(sign_check_data)
  if signature_check:
    palletInDb.production(data={
      'id_pallet': parameters.id_pallet,
      'product_name':parameters.product_name,
      'product_batch': parameters.product_batch,
      'thing_quantity': parameters.thing_quantity,
      'data_of_manufacture': parameters.data_of_manufacture,
      'expiration_date': parameters.expiration_date
      })
  else:
    return {'message': 'invalid_signature'}


@app.post('/change_pallet_status') 
async def change_pallet_status(parameters: QrCode):
  sign_check_data = {
    'signature': parameters.signature,
    'timestamp': parameters.timestamp,
    'api_key': parameters.api_common_key
  }
  signature_check = check_signature(sign_check_data)
  if signature_check:
    palletInDb.change_pallet_status(id_pallet=parameters.id_pallet)
  else:
    return {'message': 'invalid_signature'}

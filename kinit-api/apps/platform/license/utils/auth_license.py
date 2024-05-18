from pydantic import BaseModel
from datetime import datetime, timedelta
from Crypto.Cipher import AES
import base64

key = 'feffrrwrvvwca1dfg1Ufwrqrrty1234f'


def pad(s):
    return s + (16 - len(s) % 16) * chr(16 - len(s) % 16)


def unpad(s):
    return s[:-ord(s[len(s) - 1:])]


def generate_license(device_id, validity_days):
    cipher = AES.new(key.encode('utf-8'), AES.MODE_ECB)
    expire_time = (datetime.now() + timedelta(days=validity_days)).timestamp()
    data = f"{device_id},{expire_time}"
    encrypted_data = cipher.encrypt(pad(data).encode('utf-8'))
    return base64.b64encode(encrypted_data).decode('utf-8')


def decode_license(license_key):
    cipher = AES.new(key.encode('utf-8'), AES.MODE_ECB)
    decrypted_data = unpad(cipher.decrypt(base64.b64decode(license_key)).decode('utf-8'))
    device_id, expire_time = decrypted_data.split(',')
    return device_id, float(expire_time)


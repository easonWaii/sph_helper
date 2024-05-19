import ctypes
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
# 加载so库
lib = ctypes.CDLL(os.path.join(current_dir, 'liblicense.so'))


def decode_license(device_id, license_key):
    return lib.verify_license(device_id.encode('utf-8'), license_key.encode('utf-8'))

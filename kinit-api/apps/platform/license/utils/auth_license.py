import ctypes

# 加载共享库
lib = ctypes.CDLL('./liblicense.so')


def decode_license(device_id, license_key):
    return lib.verify_license(device_id.encode('utf-8'), license_key.encode('utf-8'))

import time
from services.encryption_service import generate_key

def rotate_key():
    while True:
        time.sleep(60)
        generate_key()
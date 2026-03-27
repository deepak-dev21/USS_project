from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher = Fernet(key)

def generate_key():
    global key, cipher
    key = Fernet.generate_key()
    cipher = Fernet(key)
    return key.decode()

def encrypt(data):
    return cipher.encrypt(data.encode()).decode()

def decrypt(data):
    return cipher.decrypt(data.encode()).decode()
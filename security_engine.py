import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import os

# In a real app, this key would be stored in a secure environment variable
MASTER_PASSWORD = b"super-secret-master-key"
SALT = b"constant-salt-for-demo" # In production, use unique salts

def generate_key():
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=SALT,
        iterations=100000,
    )
    return base64.urlsafe_b64encode(kdf.derive(MASTER_PASSWORD))

cipher_suite = Fernet(generate_key())

def encrypt_data(data):
    if not data: return None
    if isinstance(data, int): data = str(data)
    return cipher_suite.encrypt(data.encode()).decode()

def decrypt_data(encrypted_data):
    if not encrypted_data: return None
    try:
        return cipher_suite.decrypt(encrypted_data.encode()).decode()
    except Exception:
        return "[DECRYPTION_FAILED]"

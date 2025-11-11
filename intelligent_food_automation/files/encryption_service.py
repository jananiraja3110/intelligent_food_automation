import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64

class EncryptionService:
    @staticmethod
    def generate_key():
        """Generate a new encryption key"""
        return Fernet.generate_key()
    
    @staticmethod
    def encrypt_file(file_data, key):
        """Encrypt file data using the provided key"""
        fernet = Fernet(key)
        encrypted_data = fernet.encrypt(file_data)
        return encrypted_data
    
    @staticmethod
    def decrypt_file(encrypted_data, key):
        """Decrypt file data using the provided key"""
        fernet = Fernet(key)
        decrypted_data = fernet.decrypt(encrypted_data)
        return decrypted_data
    
    @staticmethod
    def get_file_type(filename):
        """Determine file type based on extension"""
        extension = filename.lower().split('.')[-1]
        if extension in ['xlsx', 'xls']:
            return 'excel'
        elif extension == 'csv':
            return 'csv'
        elif extension in ['txt', 'json', 'xml']:
            return 'dataset'
        else:
            return 'other'
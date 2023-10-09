from cryptography.fernet import Fernet
import sqlite3

class Users():
    def __init__(self, username, openkey):
        self.username = username
        self.openkey = openkey
        self.enckey = Fernet.generate_key()  # Schlüssel zur Verschlüsselung generieren
        self.cipher_suite = Fernet(self.enckey)
        self.conn = sqlite3.connect('users.db')
        self.c = self.conn.cursor()
        self.c.execute('''CREATE TABLE IF NOT EXISTS users (username text, encrypted_key text)''')
        self.conn.commit()
        self.save_user()

    def save_user(self):
        encrypted_key = self.encrypt_key(self.openkey)  # OpenAI API-Schlüssel verschlüsseln
        self.c.execute("INSERT INTO users (username, encrypted_key) VALUES (?, ?)", (self.username, encrypted_key))
        self.conn.commit()

    def encrypt_key(self, api_key):
        encrypted_key = self.cipher_suite.encrypt(api_key.encode())
        return encrypted_key.decode()

    def decrypt_key(self, encrypted_key):
        decrypted_key = self.cipher_suite.decrypt(encrypted_key.encode())
        return decrypted_key.decode()

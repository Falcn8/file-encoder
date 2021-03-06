from cryptography.fernet import Fernet

class Encryptor():
    def key_create(self):
        key = Fernet.generate_key()
        return key

    def key_write(self, key, key_name):
        with open(key_name, 'wb') as mykey:
            mykey.write(key)

    def key_load(self, key_name):
        with open(key_name, 'rb') as mykey:
            key = mykey.read()
        return key

    def file_encrypt(self, key, original_file, encrypted_file):
        f = Fernet(key)
        with open(original_file, 'rb') as file:
            original = file.read()
        encrypted = f.encrypt(original)
        with open (encrypted_file, 'wb') as file:
            file.write(encrypted)

    def file_decrypt(self, key, encrypted_file, decrypted_file):
        f = Fernet(key)
        with open(encrypted_file, 'rb') as file:
            encrypted = file.read()
        decrypted = f.decrypt(encrypted)
        with open(decrypted_file, 'wb') as file:
            file.write(decrypted)

if __name__ == "__main__":
    crypt = input("Encrypt or decrypt (e/d)\n>>> ")
    if crypt == "e":
        file = input("Enter the file to encrypt\n>>> ")
        encryptor = Encryptor()
        mykey = encryptor.key_create()
        encryptor.key_write(mykey, 'key.key')
        loaded_key = encryptor.key_load('key.key')
        encryptor.file_encrypt(loaded_key, file, file)
        input("Success\nPress enter to exit...")
    elif crypt == "d":
        file = input("Enter the file to decrypt\n>>> ")
        encryptor = Encryptor()
        loaded_key = encryptor.key_load('key.key')
        encryptor.file_decrypt(loaded_key, file, file)
        input("Success\nPress enter to exit...")

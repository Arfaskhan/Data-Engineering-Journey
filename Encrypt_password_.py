from cryptography.fernet import Fernet


class Fakestr(str):
    def __str__(self):
        return '*******'

    def __repr__(self):
        return '******'


def Encrypt_password(password):
    key = open('Bytekey.key', 'rb').read()
    fernet_key = Fernet(key)
    encrypted_pass = fernet_key.encrypt(password.encode())
    with open('encrypted_pass.key', 'wb') as file:
        file.write(encrypted_pass)
    return encrypted_pass


def Decrypted_password(encrypted_pass):
    key = open('Bytekey.key', 'rb').read()
    fernet_key = Fernet(key)
    decrypted_pass = fernet_key.decrypt(encrypted_pass).decode()

    return Fakestr(decrypted_pass)


def get_decrypted_password():
    decryped_pass = Decrypted_password(open('encrypted_pass.key', 'rb').read())
    return decryped_pass

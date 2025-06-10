import sys

from cryptography.fernet import Fernet

from Encrypt_password_ import Encrypt_password


def generate_key():
    key = Fernet.generate_key()
    with open('Bytekey.key','wb') as file:
        file.write(key)
    print(f"Key generated successfully!!!")

an = 0
if an ==1 :
    if len(sys.argv )> 1:
        generate_key()

        password = sys.argv[1]
        encrypt = Encrypt_password(password)
        print(f"your passwordd succesfully encrypted ; {encrypt}")
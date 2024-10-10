from cryptography.fernet import Fernet

# opening the key
with open('filekey.key', 'rb') as filekey:
    key = filekey.read()
 
# using the generated key
fernet = Fernet(key)


with open('my-file.txt', 'rb') as encrypted_file:
    encrypted = encrypted_file.read()

decrypted = fernet.decrypt(encrypted)

#opening the file in write mode and writting the decrypted data
with open('my-file.txt', 'wb') as decrypted_file:
    decrypted_file.write(decrypted)
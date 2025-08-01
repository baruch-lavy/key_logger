from cryptography.fernet import Fernet

key = Fernet.generate_key()

with open('mykey.key', 'wb') as mykey:
    mykey.write(key)

with open('mykey.key', 'rb') as mykey:
    key = mykey.read()

print(key)

f = Fernet(key)

with open('log.csv', 'rb') as original_file:
    original = original_file.read()

encrypted = f.encrypt(original)

with open('enc_data.csv', 'wb') as encrypyed_file:
    encrypyed_file.write(encrypted)

f = Fernet(key)

with open('enc_data.csv', 'rb') as encrypyed_file:
     encrypted = encrypyed_file.read()

decrypted = f.decrypt(encrypted)

with open('dec_data.csv', 'wb') as decrypted_file:
     decrypted_file.write(decrypted)
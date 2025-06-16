import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters

chars  = list(chars)
key = chars.copy()
random.shuffle(key)


plain_txt = input("enter massage to encrypt: ")

#ENCRYPT
def encrypt(plain_txt):
    cipher_txt = ''
    for letter in plain_txt:
        index = chars.index(letter)
        cipher_txt += key[index]
    return cipher_txt

#   DECRYPT
def decrypt(cipher_txt):
    decoded_txt = ''
    for letter in cipher_txt:
        index = key.index(letter)
        decoded_txt += chars[index]
    return decoded_txt

cipher = encrypt(plain_txt)
decrypted = decrypt(cipher)

print("Encrypted:", cipher)
print("Decrypted:", decrypted)

import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)

key = chars.copy()

random.shuffle(key)

#print(f"chars : {chars}")
#print(f"key   : {key}")

#ENCRIPTION

plain_text = input("Enter a message to encrypt: ")
cifer_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cifer_text += key[index]

print(f"Original message: {plain_text}")
print(f"Encrypted message: {cifer_text}")

#DECRIPTION

cifer_text = input("Enter the encrypted message to decrypt: ")
plain_text = ""

for letter in cifer_text:
    index = key.index(letter)
    plain_text += chars[index]

print(f"Incripted message: {cifer_text}")
print(f"Decrypted message: {plain_text}")

from Crypto.Cipher import DES3
from Crypto.Util.Padding import pad
import os

key = DES3.adjust_key_parity(os.urandom(24))
iv = os.urandom(8)

text = input("Enter message: ").encode()
cipher = DES3.new(key, DES3.MODE_CBC, iv)

encrypted = cipher.encrypt(pad(text, 8))

print("Encrypted bytes:", encrypted.hex())

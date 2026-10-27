import numpy as np

K = np.array([[9, 4], [5, 7]])
K_inv = (pow(43, -1, 26) *
         np.array([[7, -4], [-5, 9]])) % 26

text = input("Enter message: ").upper()
text = "".join(ch for ch in text if ch.isalpha()).replace("J", "I")

if len(text) % 2:
    text += "X"

cipher = ""

for i in range(0, len(text), 2):
    p = np.array([[ord(text[i])-65], [ord(text[i+1])-65]])
    c = K @ p % 26
    cipher += chr(int(c[0, 0])+65) + chr(int(c[1, 0])+65)

print("Encrypted message:", cipher)

plain = ""

for i in range(0, len(cipher), 2):
    c = np.array([[ord(cipher[i])-65], [ord(cipher[i+1])-65]])
    p = K_inv @ c % 26
    plain += chr(int(p[0, 0])+65) + chr(int(p[1, 0])+65)

print("Decrypted message:", plain)

import math

def decrypt(text, a, b):
    inv = pow(a, -1, 26)
    result = ""

    for ch in text:
        if ch.isalpha():
            c = ord(ch) - 65
            result += chr(((inv * (c - b)) % 26) + 65)
        else:
            result += ch

    return result

text = input("Enter ciphertext: ").upper()

for a in range(1, 26):
    if math.gcd(a, 26) == 1:
        for b in range(26):
            print("a =", a, "b =", b, ":", decrypt(text, a, b))

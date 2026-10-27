def encrypt(text, key):
    return ''.join(
        chr((ord(c) - 97 + k) % 26 + 97)
        for c, k in zip(text.replace(" ", "").lower(), key)
    )

plain = "send more money"
key = [9, 0, 1, 7, 23, 15, 21, 14, 11, 11, 2, 8, 9]

cipher = encrypt(plain, key)
print("Ciphertext:", cipher)

target = "cash not needed".replace(" ", "")
target = target.lower()
new_key = [(ord(c) - ord(p)) % 26
           for p, c in zip(target, cipher)]

print("Key for target plaintext:", new_key)

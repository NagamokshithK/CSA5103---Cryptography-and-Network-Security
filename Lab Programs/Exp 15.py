text = input("Enter ciphertext: ").upper()
top = int(input("Number of results: "))

results = []

for k in range(26):
    plain = ''.join(
        chr((ord(c) - 65 - k) % 26 + 65) if c.isalpha() else c
        for c in text
    )
    results.append((k, plain))

for k, plain in results[:top]:
    print("Key:", k, "Plaintext:", plain)

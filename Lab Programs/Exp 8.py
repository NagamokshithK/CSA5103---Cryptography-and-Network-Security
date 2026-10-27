plain = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
key = "CIPHER"
cipher = ""

for ch in key + plain:
    if ch not in cipher:
        cipher += ch

text = input("Enter message: ").upper()
result = ""

for ch in text:
    if ch in plain:
        result += cipher[plain.index(ch)]
    else:
        result += ch

print("Cipher alphabet:", cipher)
print("Encrypted message:", result)

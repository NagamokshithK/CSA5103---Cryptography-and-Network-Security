text = input("Enter message: ").upper()
key = input("Enter key: ").upper()
result = ""
j = 0

for ch in text:
    if ch.isalpha():
        k = ord(key[j % len(key)]) - 65
        result += chr((ord(ch) - 65 + k) % 26 + 65)
        j += 1
    else:
        result += ch

print("Encrypted message:", result)

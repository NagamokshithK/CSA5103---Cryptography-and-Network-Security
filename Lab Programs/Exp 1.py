text = input("Enter message: ")
k = int(input("Enter key (1-25): "))
result = ""

for ch in text:
    if ch.isupper():
        result += chr((ord(ch) - 65 + k) % 26 + 65)
    elif ch.islower():
        result += chr((ord(ch) - 97 + k) % 26 + 97)
    else:
        result += ch

print("Encrypted message:", result)


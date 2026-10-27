key = "KXJEYUREB ZWFHE"
alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
s = ""

for ch in key + alphabet:
    if ch in alphabet and ch not in s:
        s += ch

matrix = [s[i:i+5] for i in range(0, 25, 5)]

text = input("Enter ciphertext: ").upper()
text = "".join(ch for ch in text if ch.isalpha())

def pos(ch):
    for r in range(5):
        for c in range(5):
            if matrix[r][c] == ch:
                return r, c

out = ""

for i in range(0, len(text)-1, 2):
    a, b = text[i], text[i+1]
    r1, c1 = pos(a)
    r2, c2 = pos(b)

    if r1 == r2:
        out += matrix[r1][(c1-1)%5] + matrix[r2][(c2-1)%5]
    elif c1 == c2:
        out += matrix[(r1-1)%5][c1] + matrix[(r2-1)%5][c2]
    else:
        out += matrix[r1][c2] + matrix[r2][c1]

print("Decrypted message:", out)

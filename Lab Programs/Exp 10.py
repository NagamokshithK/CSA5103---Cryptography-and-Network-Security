matrix = [
    "MFHIK",
    "UNOPQ",
    "ZVWXY",
    "ELARG",
    "DSTBC"
]

text = input("Enter message: ").upper().replace("J", "I")
text = "".join(ch for ch in text if ch.isalpha())

pairs = []
i = 0

while i < len(text):
    a = text[i]

    if i + 1 == len(text):
        b = "X"
        i += 1
    elif text[i] == text[i+1]:
        b = "X"
        i += 1
    else:
        b = text[i+1]
        i += 2

    pairs.append((a, b))

def pos(ch):
    for r in range(5):
        for c in range(5):
            if matrix[r][c] == ch:
                return r, c

out = ""

for a, b in pairs:
    r1, c1 = pos(a)
    r2, c2 = pos(b)

    if r1 == r2:
        out += matrix[r1][(c1+1)%5] + matrix[r2][(c2+1)%5]
    elif c1 == c2:
        out += matrix[(r1+1)%5][c1] + matrix[(r2+1)%5][c2]
    else:
        out += matrix[r1][c2] + matrix[r2][c1]

print("Encrypted message:", out)

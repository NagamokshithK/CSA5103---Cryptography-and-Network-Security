import math

text = input("Enter message: ").upper()
a = int(input("Enter a: "))
b = int(input("Enter b: "))

if math.gcd(a, 26) != 1:
    print("Invalid value of a")
else:
    result = ""
    for ch in text:
        if ch.isalpha():
            p = ord(ch) - 65
            result += chr(((a * p + b) % 26) + 65)
        else:
            result += ch
    print("Encrypted message:", result)

print("b can be any integer; values modulo 26 are distinct.")
print("Valid a values:", [x for x in range(1, 26)
                          if math.gcd(x, 26) == 1])

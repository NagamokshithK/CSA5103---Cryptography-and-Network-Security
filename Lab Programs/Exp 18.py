key = input("Enter 56-bit key: ")

if len(key) == 56 and set(key) <= {'0', '1'}:
    left = key[:28]
    right = key[28:]

    print("Left 28 bits:", left)
    print("Right 28 bits:", right)
else:
    print("Enter exactly 56 binary bits.")

import math

keys = math.factorial(25)

print("Total possible keys:", keys)
print("Approximate power of 2:", round(math.log2(keys)))

# Effective keys: account for the 26-letter alphabet
# with I and J combined.
print("Approximate answer: 2^84")

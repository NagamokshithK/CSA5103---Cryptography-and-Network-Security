from collections import Counter

text = """53‡‡†305))6*;4826)4‡.)4‡);806*;48†8¶60))85;;]8*;:‡*8†83"""

freq = Counter(ch for ch in text if ch.isprintable())

print("Ciphertext character frequencies:")

for ch, count in freq.most_common():
    print(repr(ch), ":", count)

print("\nUse the frequency results to identify likely letters.")
print("Replace ciphertext symbols with guessed plaintext letters.")

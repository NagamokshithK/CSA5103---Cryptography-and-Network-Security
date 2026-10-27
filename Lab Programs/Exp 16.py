from collections import Counter

text = input("Enter ciphertext: ").upper()
frequency = Counter(c for c in text if c.isalpha())

english = "ETAOINSHRDLCUMWFGYPBVKJXQZ"
letters = [c for c, n in frequency.most_common()]
mapping = dict(zip(letters, english))

plain = ''.join(mapping.get(c, c) for c in text)

print("Frequency:", frequency)
print("Possible plaintext:", plain)

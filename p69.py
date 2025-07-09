# 69. Remove All Vowels from a String
text = input("Enter a string: ")
vowels = "aeiouAEIOU"
no_vowels = ''.join(c for c in text if c not in vowels)
print("Without vowels:", no_vowels)

# 29. Count Vowels and Consonants in a String
text = input("Enter a string: ").lower()
vowels = sum(1 for ch in text if ch in 'aeiou')
consonants = sum(1 for ch in text if ch.isalpha() and ch not in 'aeiou')
print("Vowels:", vowels)
print("Consonants:", consonants)

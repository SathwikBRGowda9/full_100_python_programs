# 28. Check if a Character is Vowel or Consonant
ch = input("Enter a character: ").lower()
if ch in 'aeiou':
    print("Vowel")
elif ch.isalpha():
    print("Consonant")
else:
    print("Not an alphabet")

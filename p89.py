# 89. Check if a String is Pangram
import string
text = input("Enter a string: ").lower()
if all(char in text for char in string.ascii_lowercase):
    print("Pangram")
else:
    print("Not a Pangram")

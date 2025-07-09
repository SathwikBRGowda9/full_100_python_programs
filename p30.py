# 30. Remove Punctuation from a String
import string
text = input("Enter a string: ")
clean_text = ''.join(ch for ch in text if ch not in string.punctuation)
print("Without punctuation:", clean_text)

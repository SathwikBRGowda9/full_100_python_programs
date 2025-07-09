# 34. Check if String is Digit, Alpha, or Alphanumeric
text = input("Enter a string: ")
if text.isdigit():
    print("All characters are digits")
elif text.isalpha():
    print("All characters are alphabets")
elif text.isalnum():
    print("Alphanumeric string")
else:
    print("Contains special characters")

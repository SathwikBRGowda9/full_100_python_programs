# 40. Check if a List is Palindrome
items = input("Enter list items separated by space: ").split()
if items == items[::-1]:
    print("List is a Palindrome")
else:
    print("Not a Palindrome")

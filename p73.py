# 73. Check if Two Strings are Anagrams
str1 = input("Enter first string: ").replace(" ", "").lower()
str2 = input("Enter second string: ").replace(" ", "").lower()
if sorted(str1) == sorted(str2):
    print("Anagram")
else:
    print("Not an Anagram")

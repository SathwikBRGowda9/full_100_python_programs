# 88. Get All Substrings of a String
text = input("Enter a string: ")
print("Substrings:")
for i in range(len(text)):
    for j in range(i + 1, len(text) + 1):
        print(text[i:j])

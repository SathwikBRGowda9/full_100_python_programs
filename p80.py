# 80. Merge Two Dictionaries
dict1 = eval(input("Enter first dictionary (e.g., {'a': 1}): "))
dict2 = eval(input("Enter second dictionary (e.g., {'b': 2}): "))
merged = {**dict1, **dict2}
print("Merged Dictionary:", merged)

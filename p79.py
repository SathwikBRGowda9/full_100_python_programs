# 79. Create a Dictionary from Two Lists
keys = input("Enter keys separated by space: ").split()
values = input("Enter values separated by space: ").split()
dictionary = dict(zip(keys, values))
print("Dictionary:", dictionary)

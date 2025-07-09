# 39. Remove Duplicates from a List
items = list(map(int, input("Enter list items separated by space: ").split()))
unique_items = list(set(items))
print("List without duplicates:", unique_items)

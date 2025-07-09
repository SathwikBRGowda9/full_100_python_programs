# 76. Find Common Elements in Two Lists
list1 = input("Enter first list (space-separated): ").split()
list2 = input("Enter second list (space-separated): ").split()
common = list(set(list1) & set(list2))
print("Common elements:", common)

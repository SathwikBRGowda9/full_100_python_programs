# 47. Remove All Occurrences of a Specific Element from List
nums = list(map(int, input("Enter numbers separated by space: ").split()))
target = int(input("Enter number to remove: "))
filtered = [n for n in nums if n != target]
print("Updated List:", filtered)

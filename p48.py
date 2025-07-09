# 48. Find Duplicate Elements in a List
nums = list(map(int, input("Enter numbers separated by space: ").split()))
duplicates = list(set([n for n in nums if nums.count(n) > 1]))
print("Duplicates:", duplicates)

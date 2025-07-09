# 71. Check if a List is Sorted
nums = list(map(int, input("Enter numbers separated by space: ").split()))
if nums == sorted(nums):
    print("List is sorted")
else:
    print("List is not sorted")

# 72. Find the Median of a List
nums = sorted(list(map(int, input("Enter numbers separated by space: ").split())))
n = len(nums)
if n % 2 == 0:
    median = (nums[n//2 - 1] + nums[n//2]) / 2
else:
    median = nums[n//2]
print("Median:", median)

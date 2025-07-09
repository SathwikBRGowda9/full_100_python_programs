# 43. Find the Second Largest Number in a List
nums = list(set(map(int, input("Enter numbers separated by space: ").split())))
if len(nums) < 2:
    print("Not enough unique numbers")
else:
    nums.sort()
    print("Second Largest:", nums[-2])

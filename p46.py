# 46. Count Even and Odd Numbers in a List
nums = list(map(int, input("Enter numbers separated by space: ").split()))
evens = sum(1 for n in nums if n % 2 == 0)
odds = len(nums) - evens
print("Even Count:", evens)
print("Odd Count:", odds)

# 44. Print Even Numbers in a List
nums = list(map(int, input("Enter numbers separated by space: ").split()))
evens = [n for n in nums if n % 2 == 0]
print("Even Numbers:", evens)

# 45. Print Odd Numbers in a List
nums = list(map(int, input("Enter numbers separated by space: ").split()))
odds = [n for n in nums if n % 2 != 0]
print("Odd Numbers:", odds)

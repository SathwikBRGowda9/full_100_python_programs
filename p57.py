# 57. Multiply All Numbers in a List
nums = list(map(int, input("Enter numbers separated by space: ").split()))
result = 1
for num in nums:
    result *= num
print("Product:", result)

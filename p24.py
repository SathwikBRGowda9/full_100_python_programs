# 24. Find All Factors of a Number
num = int(input("Enter a number: "))
print("Factors:", [i for i in range(1, num + 1) if num % i == 0])

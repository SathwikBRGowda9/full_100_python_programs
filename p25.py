# 25. Check if a Number is Perfect
num = int(input("Enter a number: "))
sum_factors = sum(i for i in range(1, num) if num % i == 0)
if sum_factors == num:
    print("Perfect Number")
else:
    print("Not a Perfect Number")

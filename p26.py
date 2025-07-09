# 26. Check if a Number is Strong Number
# (Sum of factorials of digits equals the number)
import math
num = int(input("Enter a number: "))
sum_fact = sum(math.factorial(int(d)) for d in str(num))
if sum_fact == num:
    print("Strong Number")
else:
    print("Not a Strong Number")

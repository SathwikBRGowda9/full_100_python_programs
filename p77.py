# 77. Check if a Number is a Perfect Square
import math
num = int(input("Enter a number: "))
if math.isqrt(num)**2 == num:
    print("Perfect Square")
else:
    print("Not a Perfect Square")

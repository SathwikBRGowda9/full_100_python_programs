# 17. Sum of Digits of a Number
num = input("Enter a number: ")
sum_digits = sum(int(d) for d in num)
print("Sum of digits:", sum_digits)
# 91. Check if a Number is Binary (only 0 and 1)
num = input("Enter a number: ")
if all(d in '01' for d in num):
    print("Binary Number")
else:
    print("Not a Binary Number")

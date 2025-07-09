# 13. Check Armstrong Number
num = int(input("Enter a number: "))
order = len(str(num))
sum_val = sum(int(digit) ** order for digit in str(num))
if sum_val == num:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
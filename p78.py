# 78. Count Even and Odd Digits in a Number
num = input("Enter a number: ")
even = sum(1 for d in num if d.isdigit() and int(d) % 2 == 0)
odd = sum(1 for d in num if d.isdigit() and int(d) % 2 != 0)
print("Even digits:", even)
print("Odd digits:", odd)

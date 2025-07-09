# 74. Calculate Compound Interest
p = float(input("Enter principal: "))
r = float(input("Enter annual interest rate (%): "))
t = float(input("Enter time (in years): "))
n = float(input("Enter number of times interest is compounded per year: "))
ci = p * (1 + r / (100 * n)) ** (n * t)
print("Compound Interest:", round(ci, 2))

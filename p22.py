# 22. Find HCF (GCD) of Two Numbers
def hcf(x, y):
    while y:
        x, y = y, x % y
    return x

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("HCF:", hcf(a, b))

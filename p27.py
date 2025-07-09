# 27. Calculate Power Using Recursion
def power(base, exp):
    return 1 if exp == 0 else base * power(base, exp - 1)

b = int(input("Enter base: "))
e = int(input("Enter exponent: "))
print("Result:", power(b, e))

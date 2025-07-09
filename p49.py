# 49. Create a List of Squares from 1 to n
n = int(input("Enter a number: "))
squares = [i**2 for i in range(1, n + 1)]
print("Squares List:", squares)

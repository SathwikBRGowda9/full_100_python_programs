# 83. Print an Inverted Triangle Pattern of Stars
n = int(input("Enter number of rows: "))
for i in range(n, 0, -1):
    print("*" * i)

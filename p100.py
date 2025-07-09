# 100. Print Table of Squares and Cubes from 1 to n
n = int(input("Enter a number: "))
print("Number | Square | Cube")
for i in range(1, n + 1):
    print(f"{i:^6} | {i**2:^6} | {i**3:^5}")

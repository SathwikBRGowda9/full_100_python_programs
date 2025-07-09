# 68. Count Uppercase and Lowercase Letters in a String
text = input("Enter a string: ")
upper = sum(1 for c in text if c.isupper())
lower = sum(1 for c in text if c.islower())
print("Uppercase:", upper)
print("Lowercase:", lower)

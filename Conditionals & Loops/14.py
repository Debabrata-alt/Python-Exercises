# Write a Python program to create the multiplication table (from 1 to 10) of a number.
# Expected Output:

def calculate(num, n1, n2):
  for i in range(n1, n2 + 1):
    print(f"{num} * {i} = {num * i}")

calculate(6, 1, 10)

# 6 * 1 = 6
# 6 * 2 = 12
# 6 * 3 = 18
# 6 * 4 = 24
# 6 * 5 = 30
# 6 * 6 = 36
# 6 * 7 = 42
# 6 * 8 = 48
# 6 * 9 = 54
# 6 * 10 = 60
# Write a Python function to create and print a list where the values are the squares of numbers between 1 and 30 (both included).

def func(n1, n2):
  return [el ** 2 for el in range(n1, n2 + 1)]

print(func(1, 30))
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625, 676, 729, 784, 841, 900]
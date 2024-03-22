# Write a Python program to create a function that takes one argument, and that argument will be multiplied with an unknown given number.
# Sample Output:
# Double the number of 15 = 30
# Triple the number of 15 = 45
# Quadruple the number of 15 = 60
# Quintuple the number 15 = 75

def func(n):
  return lambda a: a * n

double = func(2)
triple = func(3)
quadruple = func(4)
quintuple = func(5)

print(double(15)) # 30
print(triple(15)) # 45
print(quadruple(15)) # 60
print(quintuple(15)) # 75
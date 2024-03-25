# Write a Python program to get the factorial of a non-negative integer using recursion.

def factorial(num):
  # factorial of 0 is 1
  if num == 0:
    return 1
  else:
    return num * factorial(num - 1)

print(factorial(6)) # 720
# Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.

def func(num):
  factorial = 1
  while num > 0:
    factorial *= num
    num -= 1
  return factorial

print(func(5)) # 120

#////////////////////////////////////////////////////////////////

# Using recursion 

def fac(num):
  # factorial of 0 is 1
  if num == 0:
    return 1
  else:
    return num * fac(num - 1)

print(fac(5)) # 120
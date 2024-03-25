# Write a Python program to calculate the value of 'a' to the power of 'b' using recursion.
# Test Data :
# (power(3,4) -> 81  [3*3*3*3]

def calc_pow(a, b):
  # 0 to the power any num is 0  (0 ^ 5 = 0)
  if a == 0:
    return 0
  # any num to the power 0 is 1  (5 ^ 0 = 1)
  elif b == 0:
    return 1
  else: 
    return a * calc_pow(a, b - 1)

print(calc_pow(3, 4)) # 81
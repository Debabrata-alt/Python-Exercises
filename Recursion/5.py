# Write a Python program to get the sum of a non-negative integer using recursion.
# Test Data:
# sumDigits(345) -> 12
# sumDigits(45) -> 9

def sumDigits(num):
  if num == 0:
    return 0
  else:
    return num % 10 + sumDigits(int(num / 10))

print(sumDigits(345)) # 12
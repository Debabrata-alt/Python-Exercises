# Write a Python program to calculate the sum of the positive integers of n+(n-2)+(n-4)... (until n-x =< 0) using recursion .
# Test Data:
# sum_series(6) -> 12
# sum_series(10) -> 30

def calc_sum(num):
  if num <= 0:
    return 0
  else:
    return num + calc_sum(num - 2)

print(calc_sum(6)) # 12
print(calc_sum(10)) # 30
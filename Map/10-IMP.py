# Write a Python program to compute the square of the first N Fibonacci numbers, using the map function and generate a list of the numbers.

from functools import reduce

def fibonacci(n):
  
  fib_series =lambda n: reduce(lambda x, _: x + [x[-1] + x[-2]], range(n - 2), [0, 1])
  
  return list(map(lambda el: el ** 2, fib_series(n)))


print(fibonacci(6))
# [0, 1, 1, 4, 9, 25]

print(fibonacci(10))
# [0, 1, 1, 4, 9, 25, 64, 169, 441, 1156]

print(fibonacci(12))
# [0, 1, 1, 4, 9, 25, 64, 169, 441, 1156, 3025, 7921]

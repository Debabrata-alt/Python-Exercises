# Write a Python function to check whether a number is "Perfect" or not.
# According to Wikipedia : In number theory, a perfect number is a positive integer that is equal to the sum of its proper positive divisors, that is, the sum of its positive divisors excluding the number itself (also known as its aliquot sum). Equivalently, a perfect number is a number that is half the sum of all of its positive divisors (including itself).
# Example : The first perfect number is 6, because 1, 2, and 3 are its proper positive divisors, and 1 + 2 + 3 = 6. Equivalently, the number 6 is equal to half the sum of all its positive divisors: ( 1 + 2 + 3 + 6 ) / 2 = 6. The next perfect number is 28 = 1 + 2 + 4 + 7 + 14. This is followed by the perfect numbers 496 and 8128.

def func(num):
  return sum(n for n in range(1, num) if num % n == 0) == num


print(func(6)) # True
print(func(28)) # True
print(func(496)) # True
print(func(8128)) # True

print(func(8)) # False
print(func(29)) # False
print(func(497)) # False
print(func(8132)) # False

#///////////////////////////////////////////////////////////////////////////////////////////

# List of all perfect numbers 1 - 10000

def func(n1, n2):
  return list(i for i in range(n1, n2 + 1) if sum(j for j in range(1, i) if i % j == 0) == i)

print(func(1, 10000))
# [6, 28, 496, 8128]
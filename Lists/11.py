# 17. Write a Python program to check if each number is prime in a given list of numbers. Return True if all numbers are prime otherwise False.
# Sample Data:
# ([3, 4, 7, 9]) -> False
# ([3, 5, 7, 13]) -> True
# ([1, 5, 3]) -> True


def func(list):
  return all(all(el % n != 0 for n in range(2, el)) for el in list)


print(func([3, 4, 7, 9])) # False
print(func([3, 16, 24, 11])) # False
print(func([3, 5, 7, 13])) # True
print(func([1, 5, 3])) # True
print(func([23, 29, 31])) # True
print(func([7, 81, 5])) # False

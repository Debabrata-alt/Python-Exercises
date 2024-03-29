# Write a Python program to square and cube every number in a given list of integers using Lambda.
# Original list of integers:
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Square every number of the said list:
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# Cube every number of the said list:
# [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]

myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

sq_nums = list(map(lambda el: el ** 2, myList))
cu_nums = list(map(lambda el: el ** 3, myList))

print(sq_nums)
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

print(cu_nums)
# [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
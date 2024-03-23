# Write a Python program to triple all numbers in a given list of integers. Use Python map.

nums = (1, 2, 3, 4, 5, 6, 7)

tuplex = tuple(map(lambda el: el * 3, nums))

print(tuplex)
# (3, 6, 9, 12, 15, 18, 21)


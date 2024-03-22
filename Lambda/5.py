# Write a Python program to filter a list of integers using Lambda.
# Original list of integers:
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Even numbers from the said list:
# [2, 4, 6, 8, 10]
# Odd numbers from the said list:
# [1, 3, 5, 7, 9]

myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_nums = filter(lambda el: el % 2 == 0, myList)

odd_nums = filter(lambda el: el % 2 != 0, myList)

print(list(even_nums))
# [2, 4, 6, 8, 10]

print(list(odd_nums))
# [1, 3, 5, 7, 9]
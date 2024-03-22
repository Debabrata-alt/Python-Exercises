# Write a Python program to find numbers divisible by nineteen or thirteen from a list of numbers using Lambda.
# Orginal list:
# [19, 65, 57, 39, 152, 639, 121, 44, 90, 190]
# Numbers of the above list divisible by nineteen or thirteen:
# [19, 65, 57, 39, 152, 190]

# Difference between filter() and map()

# 1. filter() function

myList = [19, 65, 57, 39, 152, 639, 121, 44, 90, 190]

sort_list = list(filter(lambda el: el % 13 == 0 or el % 19 == 0, myList))

print(sort_list)
# [19, 65, 57, 39, 152, 190]

#////////////////////////////////////////////////////////////////////////////////////////////

# 2. map() function

myList = [19, 65, 57, 39, 152, 639, 121, 44, 90, 190]

sort_list = list(map(lambda el: el % 13 == 0 or el % 19 == 0, myList))

print(sort_list)
# [True, True, True, True, True, False, False, False, False, True]

sums = sum(map(lambda el: el % 13 == 0 or el % 19 == 0, myList))

print(sums) # 6

#//////////////////////////////////////

# NOTE: 
# True == 1
# False == 0
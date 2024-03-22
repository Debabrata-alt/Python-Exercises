# Write a Python program to count the even and odd numbers in a given array of integers using Lambda.
# Original arrays:
# [1, 2, 3, 5, 7, 8, 9, 10]
# Number of even numbers in the above array: 3
# Number of odd numbers in the above array: 5

myList = [1, 2, 3, 5, 7, 8, 9, 10]

even_nums = sum(map(lambda el: el % 2 == 0, myList))

odd_nums = sum(map(lambda el: el % 2 != 0, myList))

print(even_nums) # 3
print(odd_nums) # 5

#///////////////////////////////////////////////////////////////////////////////////////

myList = [1, 2, 3, 5, 7, 8, 9, 10]

even_nums = len(list(filter(lambda el: el % 2 == 0, myList)))

odd_nums = len(list(filter(lambda el: el % 2 != 0, myList)))

print(even_nums) # 3
print(odd_nums) # 5


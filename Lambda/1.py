# Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument, also create a lambda function that multiplies argument x with argument y and prints the result.
# Sample Output:
# 25
# 48

#//////////////////////////////////////

func = lambda a: a + 15

print(func(10)) # 25

#///////////////////////////////////////

func = lambda a, b: a * b

print(func(6, 8)) # 48
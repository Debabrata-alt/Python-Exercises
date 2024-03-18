# Write a Python program to replace the last element in a list with another list.

num1 = [1, 3, 5, 7, 9, 10]
num2 = [2, 4, 6, 8]

# Update the last element of 'num1' (using slicing) to be the entire 'num2' list
# This effectively replaces the last element of 'num1' with the elements of 'num2'
num1[-1: ] = num2

print(num1) # [1, 3, 5, 7, 9, 2, 4, 6, 8]


#////////////////////////////////////////////////////////
# Negative indices - more examples

num1 = [1, 3, 5, 7, 9, 10]

print(num1[-1:]) # [10]
print(num1[-2:]) # [9, 10]
print(num1[-3:]) # [7, 9, 10]
print(num1[-4:]) # [5, 7, 9, 10]

print(num1[-1]) # 10
print(num1[-2]) # 9
print(num1[-3]) # 7
print(num1[-4]) # 5

print(num1[-2: -1]) # [9]
print(num1[-3: -1]) # [7, 9]
print(num1[-4: -1]) # [5, 7, 9]
print(num1[-5: -1]) # [3, 5, 7, 9]


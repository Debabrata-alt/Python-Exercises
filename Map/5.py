# Write a Python program to square the elements of a list using the map() function.

nums = [4, 5, 2, 9]

def square_num(n):
  return n * n

newList = list(map(square_num, nums))

print(newList)
# [16, 25, 4, 81]
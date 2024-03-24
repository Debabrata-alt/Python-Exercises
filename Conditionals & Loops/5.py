# Write a Python program to get the Fibonacci series between 0 and 50.
# Note : The Fibonacci Sequence is the series of numbers :
# 0, 1, 1, 2, 3, 5, 8, 13, 21, ....
# Every next number is found by adding up the two numbers before it.
# Expected Output : 1 1 2 3 5 8 13 21 34

myList = [0, 1]

def fibonacci(n1, n2, myList):
  for i in range(n1 + 2, n2):
    myList.append(myList[i- 1] + myList[i - 2])
  return myList

# first 10 fibonacci nums
print(fibonacci(0, 10, myList))
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

#/////////////////////////////////////////////////////////////////////////////////////////

x, y = 0, 1

while y < 50:
  print(y)
  x, y = y, x + y

# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34
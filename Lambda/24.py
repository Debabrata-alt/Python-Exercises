# Write a Python program to create the next bigger number by rearranging the digits of a given number.
# Original number: 12
# Next bigger number: 21
# Original number: 10
# Next bigger number: False
# Original number: 201
# Next bigger number: 210
# Original number: 102
# Next bigger number: 120
# Original number: 445
# Next bigger number: 454

def func(num):
  numList = list(str(num))
  
  for n in range(len(numList) - 2, -1, -1):
    if numList[n] < numList[n + 1]:
      z = numList[n:]
      y = min(filter(lambda x: x > z[0], z))
      z.remove(y)
      z.sort()
      numList[n:] = [y] + z
      nxt_biggest_no = int("".join(numList))
      return f"Next biggest number = {nxt_biggest_no}"
  return False


print(func(12))
# Next biggest number = 21

print(func(10)) # False

print(func(201))
# Next biggest number = 210

print(func(102))
# Next biggest number = 120

print(func(445))
# Next biggest number = 454


#///////////////////////////////////////////////////////////////////////////////////////

# Same process as above, we just used 'for-else' block here.

def func(num):
  numList = list(str(num))
  
  for n in range(len(numList) - 2, -1, -1):
    if numList[n] < numList[n + 1]:
      z = numList[n:]
      y = min(filter(lambda x: x > z[0], z))
      z.remove(y)
      z.sort()
      numList[n:] = [y] + z
      nxt_biggest_no = int("".join(numList))
      return f"Next biggest number = {nxt_biggest_no}"
  else: 
    return False


print(func(12))
# Next biggest number = 21

print(func(10)) # False

print(func(201))
# Next biggest number = 210

print(func(102))
# Next biggest number = 120

print(func(445))
# Next biggest number = 454


#///////////////////////////////////////////////////////////////////////////////////////

# Warning! This one below is NOT the correct solution.

from random import shuffle

def func(num):
  myList = list(str(num))
  new_num = 0
  while new_num < num:
    shuffle(myList)
    new_num = int("".join(myList))
  if new_num > num:
    return f"Next biggest number = {new_num}"
  else:
    return False

print(func(12))
# Next biggest number = 21

print(func(10)) # False

print(func(201))
# Next biggest number = 210

print(func(102))
# Next biggest number = 120

print(func(445))
# Next biggest number = 454

# Write a Python program to remove consecutive (following each other continuously) duplicates (elements) from a given list.

numList = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4, 2]

newList = list()
previous_val = None

for el in numList:
  if el != previous_val:
    newList.append(el)
  previous_val = el

print(newList)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4, 2]

#/////////////////////////////////////////////////////

numList = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4, 2]

newList = [numList[0]]

i = 1

while i <= len(numList) - 1:
  if numList[i] != numList[i - 1]:
    newList.append(numList[i])
  i += 1

print(newList)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4, 2]

#/////////////////////////////////////////////////////////////////////////////////////////////

# Import the 'groupby' function from the 'itertools' module
from itertools import groupby

def compress(list_nums):
  # Use 'groupby' to group consecutive duplicates and return the unique keys
  return [key for key, group in groupby(list_nums)] 

num_list = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]

print(compress(num_list)) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4]
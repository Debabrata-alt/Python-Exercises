# Write a Python program to calculate the sum of a list of numbers using recursion.

myList = [2, 4, 5, 6, 7]

def cal_sum(myList):
  if len(myList) == 1:
    return myList[0]
  else: 
    return myList[0] + cal_sum(myList[1:])

print(sum(myList)) # 24
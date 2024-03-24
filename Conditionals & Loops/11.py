# Write a Python program to find numbers between 100 and 400 (both included) where each digit of a number is an even number. The numbers obtained should be printed in a comma-separated sequence.

myList = []

def myFunc(n1, n2):
  for i in range(n1, n2 + 1):
    l = list(str(i))
    if all(int(e) % 2 == 0 for e in l):
      myList.append(i)
  return myList

print(myFunc(100, 400))
# [200, 202, 204, 206, 208, 220, 222, 224, 226, 228, 240, 242, 244, 246, 248, 260, 262, 264, 266, 268, 280, 282, 284, 286, 288, 400]
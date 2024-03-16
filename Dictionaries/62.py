# Write a Python program to map the values of a given list to a dictionary using a function, where the key-value pairs consist of the original value as the key and the result of the function as the value.
# Sample Output:
# {1: 1, 2: 4, 3: 27, 4: 256}

myList = [1, 2, 3, 4]

def func(myList):
  return dict(zip(myList, list(map(lambda x: x ** x, myList))))

print(func(myList))
# {1: 1, 2: 4, 3: 27, 4: 256}


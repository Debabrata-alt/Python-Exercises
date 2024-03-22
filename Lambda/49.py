# Write a Python program to remove specific words from a given list using lambda.
# Original list:
# ['orange', 'red', 'green', 'blue', 'white', 'black']
# Remove words:
# ['orange', 'black']
# After removing the specified words from the said list:
# ['red', 'green', 'blue', 'white']

myList = ['orange', 'red', 'green', 'blue', 'white', 'black']
removables = ['orange', 'black']

newList = list(filter(lambda el: el not in removables, myList))

print(newList)
# ['red', 'green', 'blue', 'white']


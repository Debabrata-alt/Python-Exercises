# Write a Python program to reverse strings in a given list of string values using lambda.
# Original lists:
# ['Red', 'Green', 'Blue', 'White', 'Black']
# Reverse strings of the said given list:
# ['deR', 'neerG', 'eulB', 'etihW', 'kcalB']

myList = ['Red', 'Green', 'Blue', 'White', 'Black']

newList = list(map(lambda el: el[::-1], myList))

print(newList)
# ['deR', 'neerG', 'eulB', 'etihW', 'kcalB']

#///////////////////////////////////////////////

myList = ['Red', 'Green', 'Blue', 'White', 'Black']

newList = list(map(lambda el: "".join(reversed(el)), myList))

print(newList)
# ['deR', 'neerG', 'eulB', 'etihW', 'kcalB']
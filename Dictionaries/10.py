# Write a Python program to map two lists into a dictionary.

keys = ['red', 'green', 'blue']

values = ['#FF0000', '#008000', '#0000FF']

myDict = dict(zip(keys, values))

print(myDict)
# {'red': '#FF0000', 'green': '#008000', 'blue': '#0000FF'}
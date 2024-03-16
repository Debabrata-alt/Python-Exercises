# Write a Python program to find the shortest list of values for the keys in a given dictionary.
# Original Dictionary: {'V': [10, 12], 'VI': [10], 'VII': [10, 20, 30, 40], 'VIII': [20], 'IX': [10, 30, 50, 70], 'X': [80]} Shortest list of values with the keys of the said dictionary: ['VI', 'VIII', 'X']

myDict = {'V': [10, 12], 'VI': [10], 'VII': [10, 20, 30, 40], 'VIII': [20], 'IX': [10, 30, 50, 70], 'X': [80]}

l = sorted(myDict, key=lambda x: len(myDict[x]))

print(l) # ['VI', 'VIII', 'X', 'V', 'VII', 'IX']

#///////////////////////////////////////////////////////////////////////////////////

myDict = {'V': [10, 12], 'VI': [10], 'VII': [10, 20, 30, 40], 'VIII': [20], 'IX': [10, 30, 50, 70], 'X': [80]}

l = [k for k, v in myDict.items() if len(v) == 1]

print(l)
# ['VI', 'VIII', 'X']



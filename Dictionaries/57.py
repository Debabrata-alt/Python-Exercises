# Write a Python program to get the total length of all values in a given dictionary with string values.
# Original dictionary:
# {'#FF0000': 'Red', '#800000': 'Maroon', '#FFFF00': 'Yellow', '#808000': 'Olive'}
# Total length of all values of the said dictionary with string values:
# 20

myDict = {'#FF0000': 'Red', '#800000': 'Maroon', '#FFFF00': 'Yellow', '#808000': 'Olive'}

# sum of the length of all keys
l = sum(map(len, myDict))

print(l) # 28

# sum of the length of all values
x = sum(map(lambda x: len(myDict[x]), myDict))

print(x) # 20

# sum of the length of all keys and values together
y = sum(map(lambda x: len(x) + len(myDict[x]), myDict))

print(y) # 48

#/////////////////////////////////////////////////////////////////////////////////////////////

myDict = {'#FF0000': 'Red', '#800000': 'Maroon', '#FFFF00': 'Yellow', '#808000': 'Olive'}

# sum of the length of all values
z = sum(len(value) for value in myDict.values())

print(z) # 20
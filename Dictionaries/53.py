# Write a Python program to count the frequency of a dictionary.
# Original Dictionary:
# {'V': 10, 'VI': 10, 'VII': 40, 'VIII': 20, 'IX': 70, 'X': 80, 'XI': 40, 'XII': 20}
# Count the frequency of the said dictionary:
# Counter({10: 2, 40: 2, 20: 2, 70: 1, 80: 1})

myDict = {'V': 10, 'VI': 10, 'VII': 40, 'VIII': 20, 'IX': 70, 'X': 80, 'XI': 40, 'XII': 20}

myList = []
newDict = {}

for v in myDict.values():
  myList.append(v)

for i in myList:
  newDict[i] = myList.count(i)

print(newDict)
# {10: 2, 40: 2, 20: 2, 70: 1, 80: 1}

#////////////////////////////////////////////////////////////////////////////////////

myDict = {'V': 10, 'VI': 10, 'VII': 40, 'VIII': 20, 'IX': 70, 'X': 80, 'XI': 40, 'XII': 20}

newDict = {}
finalDict = {}

count = 1

for key, value in myDict.items():
  if value in newDict.values():
    count += 1
    finalDict[value] = count
  else:
    finalDict[value] = 1
    newDict[key] = value


print(finalDict)
# {10: 2, 40: 3, 20: 4, 70: 1, 80: 1}

print(newDict)
# {'V': 10, 'VI': 10, 'VII': 40, 'VIII': 20, 'IX': 70, 'X': 80, 'XI': 40, 'XII': 20}

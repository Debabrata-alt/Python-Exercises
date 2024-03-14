# Write a Python program to sort Counter by value.
# Sample data : {'Math':81, 'Physics':83, 'Chemistry':87}
# Expected data: [('Chemistry', 87), ('Physics', 83), ('Math', 81)]

myDict = {'Math':81, 'Physics':83, 'Chemistry':87}

l = sorted(myDict.items(), key=lambda el: el[1], reverse=True)

print(l) 
# [('Chemistry', 87), ('Physics', 83), ('Math', 81)]

#/////////////////////////////////////////////////////////////////////

x = sorted(myDict, key=lambda el: myDict[el], reverse=True)

print(x)
# ['Chemistry', 'Physics', 'Math']

#/////////////////////////////////////////////////////////////////////

y = sorted(myDict.values(), reverse=True)

print(y) 
# [87, 83, 81]
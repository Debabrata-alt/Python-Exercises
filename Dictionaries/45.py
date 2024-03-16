# A Python Dictionary contains List as a value. Write a Python program to update the list values in the said dictionary.
# Original Dictionary:
# {'Math': [88, 89, 90], 'Physics': [92, 94, 89], 'Chemistry': [90, 87, 93]}
# Update the list values of the said dictionary:
# {'Math': [89, 90, 91], 'Physics': [90, 92, 87], 'Chemistry': [90, 87, 93]}

myDict = {'Math': [88, 89, 90], 'Physics': [92, 94, 89], 'Chemistry': [90, 87, 93]}

# Updating myDict dictionary 

myDict["Math"] = [e + 1 for e in myDict["Math"]]

myDict["Physics"] = [e - 2 for e in myDict["Physics"]]


print(myDict)
# {'Math': [89, 90, 91], 'Physics': [90, 92, 87], 'Chemistry': [90, 87, 93]}
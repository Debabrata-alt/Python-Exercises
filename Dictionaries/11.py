# Write a Python program to sort a given dictionary by key.

myDict = {
  'red': '#FF0000',
  'green': '#008000',
  'black': '#000000',
  'white': '#FFFFFF'
}

# sort the keys of 'myDict' dictionary in lexicographical order.
sorted_myDict_keys_list = sorted(myDict)

print(sorted_myDict_keys_list)
# ['black', 'green', 'red', 'white']

#/////////////////////////////////////////////////////////////////

myDict = {
  'red': '#FF0000',
  'green': '#008000',
  'black': '#000000',
  'white': '#FFFFFF'
}

print(myDict.items())
# dict_items([('red', '#FF0000'), ('green', '#008000'), ('black', '#000000'), ('white', '#FFFFFF')])

sorted_myDict_tuples_list = sorted(myDict.items())

print(sorted_myDict_tuples_list)
# [('black', '#000000'), ('green', '#008000'), ('red', '#FF0000'), ('white', '#FFFFFF')]

#/////////////////////////////////////////////////////////////////////

myDict = {
  'red': '#FF0000',
  'green': '#008000',
  'black': '#000000',
  'white': '#FFFFFF'
}

for key in sorted(myDict):
  # Print each key-value pair where '%s' is a placeholder for the key and its value.
  print("%s: %s" % (key, myDict[key]))
  
  # black: #000000
  # green: #008000
  # red: #FF0000
  # white: #FFFFFF
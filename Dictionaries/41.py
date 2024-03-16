# Write a Python program to split a given dictionary of lists into lists of dictionaries.
# Original dictionary of lists:
# {'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
# Split said dictionary of lists into list of dictionaries:
# [{'Science': 88, 'Language': 77}, {'Science': 89, 'Language': 78}, {'Science': 62, 'Language': 84}, {'Science': 95, 'Language': 80}]

marks = {'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}

def list_of_dicts(marks):
  
  keys = marks.keys()
  
  print(keys) # dict_keys(['Science', 'Language'])

  vals = zip(*[marks[k] for k in keys])
  
  # print(list(vals)) # [(88, 77), (89, 78), (62, 84), (95, 80)]
  
  result = [dict(zip(keys, v)) for v in vals]
  
  return result


print(list_of_dicts(marks)) 
# [{'Science': 88, 'Language': 77}, {'Science': 89, 'Language': 78}, {'Science': 62, 'Language': 84}, {'Science': 95, 'Language': 80}]

#////////////////////////////////////////////////////////////////////////////////////

myDict = {'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}

newList = []

def func(Science, Language):
  print(Science, Language) # [88, 89, 62, 95] [77, 78, 84, 80]
  for n in range(len(Science)):
    newList.append({"Science": Science[n], "language": Language[n]})
  return newList
    

print(func(**myDict))
# {'Science': 88, 'language': 77}, {'Science': 89, 'language': 78}, {'Science': 62, 'language': 84}, {'Science': 95, 'language': 80}]

#///////////////////////////////////////////////////////////////////////////////////////////

myDict = {'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}

newList = []
myList = []
final_list = []

for key in myDict:
  newList.append(myDict[key])
  myList.append(key)

print(newList) # [[88, 89, 62, 95], [77, 78, 84, 80]]
print(myList) # ['Science', 'Language']

for n in range(len(newList[0])):
  final_list.append({myList[0]: newList[0][n], myList[1]: newList[1][n]})

print(final_list)
# [{'Science': 88, 'Language': 77}, {'Science': 89, 'Language': 78}, {'Science': 62, 'Language': 84}, {'Science': 95, 'Language': 80}]
# Write a Python program to extract a list of values from a given list of dictionaries.
# Original Dictionary:
# [{'Math': 90, 'Science': 92}, {'Math': 89, 'Science': 94}, {'Math': 92, 'Science': 88}]
# Extract a list of values from said list of dictionaries where subject = Science
# [92, 94, 88]
# Original Dictionary:
# [{'Math': 90, 'Science': 92}, {'Math': 89, 'Science': 94}, {'Math': 92, 'Science': 88}]
# Extract a list of values from said list of dictionaries where subject = Math
# [90, 89, 92]

myDict = [{'Math': 90, 'Science': 92}, {'Math': 89, 'Science': 94}, {'Math': 92, 'Science': 88}]

l = [v for el in myDict for k, v in el.items() if k == "Science"]

print(l) 
# [92, 94, 88]

x = list(v for el in myDict for k, v in el.items() if k == "Math")

print(x)
# [90, 89, 92]

#///////////////////////////////////////////////////////////////////////////////

myDict = [{'Math': 90, 'Science': 92}, {'Math': 89, 'Science': 94}, {'Math': 92, 'Science': 88}]

l = [el[k] for el in myDict for k in el if k == "Science"]

print(l)# [92, 94, 88]

x = list(el[k] for el in myDict for k in el if k == "Math")

print(x) 
# [90, 89, 92]
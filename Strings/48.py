# Write a Python program to remove duplicate characters from a given string.

myStr = "python exercises practice solution"

myList = list(myStr)

print(myList)
# ['p', 'y', 't', 'h', 'o', 'n', ' ', 'e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's', ' ', 'p', 'r', 'a', 'c', 't', 'i', 'c', 'e', ' ', 's', 'o', 'l', 'u', 't', 'i', 'o', 'n']

# initialize an empty list
final_list = list()

for el in myList:
  if el not in final_list or el == " ":
    final_list.append(el)

print(final_list)
# ['p', 'y', 't', 'h', 'o', 'n', ' ', 'e', 'x', 'r', 'c', 'i', 's', ' ', 'a', ' ', 'l', 'u']

newStr = "".join(final_list)

print(newStr)
# python exrcis a lu

#/////////////////////////////////////////////////////////////

myStr = "python exercises practice solution"

temp = ""

for e in myStr:
  if e not in temp:
    temp += e

print(temp) 
# python exrcisalu


#////////////////////////////////////////////////////////////////////////////////////////


# Import the OrderedDict class from the collections module
from collections import OrderedDict

# Define a function to remove duplicate characters from a string
def remove_duplicate(str1):
  
  # Create an OrderedDict object to store unique characters and their order
  unique_characters = OrderedDict.fromkeys(str1)
    
  print(unique_characters)
  # OrderedDict({'w': None, '3': None, 'r': None, 'e': None, 's': None, 'o': None, 'u':None, 'c': None}) 

  # Join the keys of the OrderedDict to form a string without duplicates
  return "".join(unique_characters.keys())



print(remove_duplicate("python exercises practice solution")) 
# python exrcisalu

print(remove_duplicate("w3resource"))
# w3resouc


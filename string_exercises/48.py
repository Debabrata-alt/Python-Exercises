# Write a Python program to remove duplicate characters from a given string.


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


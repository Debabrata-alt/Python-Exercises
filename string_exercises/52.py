# Write a Python program to find all the common characters in lexicographical order from two given lower case strings. If there are no similar letters print "No common characters".

from collections import Counter  

def common_chars(str1, str2):
  # Create Counter objects for each string
  d1 = Counter(str1)  
  d2 = Counter(str2)
  
  print(d1)
  # 1. Counter({'P': 1, 'y': 1, 't': 1, 'h': 1, 'o': 1, 'n': 1})
  # 2. Counter({'a': 2, 'J': 1, 'v': 1})
  print(d2)
  # 1. Counter({'P': 2, 'H': 1})
  # 2. Counter({'P': 2, 'H': 1})
  
  # Intersection of the counters gives common elements
  common_counter_obj = d1 & d2
  
  print(common_counter_obj) 
  # 1. Counter({'P': 1})
  # Counter()
  
  print(common_counter_obj.elements()) 
  # 1. <itertools.chain object at 0x00000270F4896140>
  # 2. <itertools.chain object at 0x0000024869246200>
  
  print(list(common_counter_obj.elements())) 
  # 1. ['P']
  # 2. []

  # If no common elements, return message 
  if len(common_counter_obj) == 0:
    return "No common characters."

  # Get list of common characters
  common_chars = list(common_counter_obj.elements())
  
  # Sort common characters
  common_chars = sorted(common_chars)

  # Join the characters into a string
  return "".join(common_chars)


print(common_chars("Python", "PHP")) # P
print(common_chars("Java", "PHP")) # No common characters.


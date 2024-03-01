# Write a Python program to find all the common characters in lexicographical order from two given lower case strings. If there are no similar letters print "No common characters".


# Import Counter for counting characters
from collections import Counter  

def common_chars(str1, str2):
  # Create Counter objects for each string
  d1 = Counter(str1)  
  d2 = Counter(str2)
  
  # Intersection of the counters gives common elements
  common_counter_obj = d1 & d2

  # If no common elements, return message 
  if len(common_counter_obj) == 0:
    return "No common characters."

  # Get list of common characters
  common_chars = list(common_counter_obj.elements())
  
  # Sort common characters
  common_chars = sorted(common_chars)

  # Join the characters into a string
  return ''.join(common_chars)


print(common_chars("Python", "PHP")) # P
print(common_chars("Java", "PHP")) # No common characters.

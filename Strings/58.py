# Write a Python program that concatenates uncommon characters from two strings.

# Function to concatenate uncommon characters
def uncommon_chars_concat(s1, s2):

  # Convert strings to sets
  set1 = set(s1)
  set2 = set(s2)

  # Intersection of set1 and set2 gives common characters
  common_chars = list(set1 & set2) 

  # List comprehension to get uncommon chars from each string
  result = [ch for ch in s1 if ch not in common_chars] + [ch for ch in s2 if ch not in common_chars]
  
  print(result) # ['p', 'q', 'r', 'x', 'y', 'z']

  # Join characters into string
  return("".join(result))


print(uncommon_chars_concat("abcdpqr", "xyzabcd")) # pqrxyz

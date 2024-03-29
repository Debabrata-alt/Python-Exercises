# Write a Python program to generate two strings from a given string. For the first string, use the characters that occur only once, and for the second, use the characters that occur multiple times in the said string.

def func(inp_str):
  uniq_dict = {char: inp_str.count(char) for char in inp_str if inp_str.count(char) == 1}
  mul_dict = {char: inp_str.count(char) for char in inp_str if inp_str.count(char) > 1}
  
  return "".join(uniq_dict), "".join(mul_dict)


uniq_chars, mul_chars = func("aabbcceffgh")

print(uniq_chars) # egh
print(mul_chars) # abcf

# NOTE: Dictionaries do not allow duplicates, so you can not have two keys with the same name in a dictionary.

#/////////////////////////////////////////////////////////////////////////////////////////////

from collections import Counter

def generateStrings(input):
  # Create a character counter dict from input
  unique_char_dict = Counter(input) 
  
  print(unique_char_dict)
  # Counter({'a': 2, 'b': 2, 'c': 2, 'f': 2, 'e': 1, 'g': 1, 'h': 1})
  
  # Part 1 contains single occurrence characters
  part1 = [key for (key,count) in unique_char_dict.items() if count == 1]
  
  print(part1) # ['e', 'g', 'h']
  
  # Part 2 contains multiple occurrence characters
  part2 = [key for (key,count) in unique_char_dict.items() if count > 1]
  
  print(part2) # ['a', 'b', 'c', 'f']

  # Sort the characters in each part
  part1.sort()
  part2.sort()

  return "".join(el for el in part1), "".join(el for el in part2)


# Generate the two strings
s1, s2 = generateStrings("aabbcceffgh")

print(s1) # egh
print(s2) # abcf

# Write a Python function to check whether a string is a pangram or not.
# Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
# For example : "The quick brown fox jumps over the lazy dog"

def func(myStr):
  all_alphabets = "abcdefghijklmnopqrstuvwxyz"
  # string is made all lowercase and then is sorted alphabetically in ascending order (from a to z)
  sort_str = "".join(sorted(myStr.lower()))
  # all whitespaces removed
  str_without_spaces = sort_str.replace(" ", "")
  
  final_str = str_without_spaces[0]
  
  for el in str_without_spaces:
    if el not in final_str:
      final_str += el
    str_without_spaces = str_without_spaces[1:]
  
  return final_str == all_alphabets


print(func("The quick brown fox jumps over the lazy dog")) # True
print(func("Pack my box with five dozen liquor jugs")) # True
print(func("The five boxing wizards jump quickly")) # True
print(func("Jackdaws love my big sphinx of quartz")) # True

print(func("Avantika go to the house as early as possible")) # False
print(func("Pinku I love you")) # False
# Write a Python program that concatenates uncommon characters from two strings.

def uncommon_chars_concat(s1, s2):
  set1 = set(s1)
  set2 = set(s2)
  # Find common characters in set1 and set2
  common_chars_set = set1.intersection(set2)
  common_chars_list = list(common_chars_set)
  # List comprehension to get uncommon chars from each string
  result = [ch for ch in s1 if ch not in common_chars_list] + [ch for ch in s2 if ch not in common_chars_list]

  # Join characters into string
  return(''.join(result))


print(uncommon_chars_concat("abcdpqr", "xyzabcd")) # pqrxyz
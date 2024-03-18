# Write a Python program to find all the common characters in lexicographical order from two given lower case strings. If there are no similar letters print "No common characters".


def common_chars(str1, str2):
  set1 = set(str1)
  set2 = set(str2)
  set3 = set1.intersection(set2)
  if len(set3) == 0:
    return "No common characters."
  else:
    return ",".join(el for el in list(set3))


print(common_chars("Python", "PHP")) # P
print(common_chars("PINKU", "PIULI")) # I,U,P
print(common_chars("Java", "PHP")) # No common characters.
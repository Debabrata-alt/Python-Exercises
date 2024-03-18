# Write a Python program to find the minimum window in a given string that will contain all the characters of another given string.
# Example 1
# Input : str1 = "PRWSOERIUSFK"
# str2 = "OSU"
# Output: Minimum window is "OERIUS"


def func(str1, str2):
  
  list_of_indices = []
  
  for s in str2:
    # First occurance of s
    index = str1.find(s)
    list_of_indices.append(index)
  
  list_of_indices.sort()
  
  return str1[list_of_indices[0]: (list_of_indices[-1] + 1)]


print(func("PRWSOERIUSFK", "OSU")) # SOERIU
print(func("Rqnzsvaytazu", "avn")) # nzsva
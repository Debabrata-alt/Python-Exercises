# Write a Python program to get the frequency of elements in a given list of lists.
# Original list of lists:
# [[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]]
# Frequency of the elements in the said list of lists:
# {1: 1, 2: 3, 3: 1, 4: 1, 5: 2, 6: 1, 7: 1, 8: 1, 9: 1}

org_list = [[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]]

def flatten(list):
  return [e for el in list for e in el]

flat_list = flatten(org_list)

# dict comprehension
dict_fren = {el: flat_list.count(el) for el in flat_list}

print(dict_fren)
# {1: 1, 2: 3, 3: 1, 4: 1, 5: 2, 6: 1, 7: 1, 8: 1, 9: 1}

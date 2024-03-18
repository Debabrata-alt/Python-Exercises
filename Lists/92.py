# Write a Python program to merge some list items in a given list using the index value.
# Original lists:
# ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# Merge items from 2 to 4 in the said List:
# ['a', 'b', 'cd', 'e', 'f', 'g']
# Merge items from 3 to 7 in the said List:
# ['a', 'b', 'c', 'defg']


chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

def merge_some_chars(inp_list, merge_from, merge_to):
  result = inp_list
  result[merge_from : merge_to] = ["".join(result[merge_from : merge_to])]
  return result


print(merge_some_chars(chars, 2, 4))
# ['a', 'b', 'cd', 'e', 'f', 'g']

print(merge_some_chars(chars, 4, 7))
# ['a', 'b', 'cd', 'e', 'fg']
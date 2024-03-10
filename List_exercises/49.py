# Write a Python program to remove duplicate dictionary entries from a given list.
# Original list with duplicate dictionary:
# [{'Green': '#008000'}, {'Black': '#000000'}, {'Blue': '#0000FF'}, {'Green': '#008000'}]
# After removing duplicate dictionary of the said list:
# [{'Black': '#000000'}, {'Blue': '#0000FF'}, {'Green': '#008000'}]


org_list = [{'Green': '#008000'}, {'Black': '#000000'}, {'Blue': '#0000FF'}, {'Green': '#008000'}]

def func(input_list):
  # remove duplicates by set comprehension (set comprehension = {})
  my_set = {tuple(el.items()) for el in input_list}
  
  print(my_set)
  # {(('Black', '#000000'),), (('Green', '#008000'),), (('Blue', '#0000FF'),)}
  
  return [dict(e) for e in my_set]


print(func(org_list))
# [{'Blue': '#0000FF'}, {'Black': '#000000'}, {'Green': '#008000'}]

#///////////////////////////////////////////////////////////////////////////////////////////

org_list = [{'Green': '#008000'}, {'Black': '#000000'}, {'Blue': '#0000FF'}, {'Green': '#008000'}]

def func(input_list):
  # Use a set comprehension to convert each dictionary in the list to a tuple and remove duplicates.
  # Then, convert the unique tuples back to dictionaries.
  return [dict(e) for e in {tuple(el.items()) for el in input_list}]


print(func(org_list))
# [{'Blue': '#0000FF'}, {'Black': '#000000'}, {'Green': '#008000'}]
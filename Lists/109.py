# Write a Python program to join adjacent members of a given list.
# Original list:
# ['1', '2', '3', '4', '5', '6', '7', '8']
# Join adjacent members of a given list:
# ['12', '34', '56', '78']
# Original list:
# ['1', '2', '3']
# Join adjacent members of a given list:
# ['12']

list1 = ['1', '2', '3', '4', '5', '6', '7', '8']
list2 = ['1', '2', '3']

def func(inp_list):
  new_list = []
  for n in range(0, len(inp_list) - 1, 2):
    new_list.append(inp_list[n] + inp_list[n + 1]) 
  return new_list


print(func(list1))
# ['12', '34', '56', '78']

print(func(list2)) # ['12']

#////////////////////////////////////////////////////////////////////////////

list1 = ['1', '2', '3', '4', '5', '6', '7', '8']
list2 = ['1', '2', '3']

def func(inp_list):
  return list(inp_list[n] + inp_list[n + 1] for n in range(0, len(inp_list) - 1, 2))


print(func(list1))
# ['12', '34', '56', '78']

print(func(list2)) # ['12']
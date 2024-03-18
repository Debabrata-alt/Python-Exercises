# Write a Python program to find the last occurrence of a specified item in a given list.
# Original list:
# ['s', 'd', 'f', 's', 'd', 'f', 's', 'f', 'k', 'o', 'p', 'i', 'w', 'e', 'k', 'c']
# Last occurrence of f in the said list:
# 7
# Last occurrence of c in the said list:
# 15
# Last occurrence of k in the said list:
# 14
# Last occurrence of w in the said list:
# 12

org_list = ['s', 'd', 'f', 's', 'd', 'f', 's', 'f', 'k', 'o', 'p', 'i', 'w', 'e', 'k', 'c']

def func(inp_list, char):
  return max(i for i, el in enumerate(inp_list) if el == char)


print(func(org_list, "f")) # 7
print(func(org_list, "c")) # 15
print(func(org_list, "k")) # 14
print(func(org_list, "w")) # 12
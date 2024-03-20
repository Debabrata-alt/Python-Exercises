# Write a Python program to convert a given tuple of positive integers into an integer.
# Original tuple:
# (1, 2, 3)
# Convert the said tuple of positive integers into an integer:
# 123
# Original tuple:
# (10, 20, 40, 5, 70)
# Convert the said tuple of positive integers into an integer:
# 102040570

tuplex1 = (1, 2, 3)
tuplex2 = (10, 20, 40, 5, 70)

def func(inp_tup):
  result = ""
  for el in inp_tup:
    result += str(el)
  return int(result)


print(func(tuplex1)) # 123
print(func(tuplex2)) # 102040570

#//////////////////////////////////////////////////////////////////////////////////////////

tuplex1 = (1, 2, 3)
tuplex2 = (10, 20, 40, 5, 70)

def func(inp_tup):
  return "".join(map(str, inp_tup))


print(func(tuplex1)) # 123
print(func(tuplex2)) # 102040570
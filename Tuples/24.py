# Write a Python program to check if a specified element appears in a tuple of tuples.
# Original list:
# (('Red', 'White', 'Blue'), ('Green', 'Pink', 'Purple'), ('Orange', 'Yellow', 'Lime'))
# Check if White presenet in said tuple of tuples!
# True
# Check if White presenet in said tuple of tuples!
# True
# Check if Olive presenet in said tuple of tuples!
# False

tuplex = (('Red', 'White', 'Blue'), ('Green', 'Pink', 'Purple'), ('Orange', 'Yellow', 'Lime'))

def func(inp_tup, n):
  return any(n in el for el in inp_tup)


print(func(tuplex, "White")) # True
print(func(tuplex, "Purple")) # True
print(func(tuplex, "Olive")) # True
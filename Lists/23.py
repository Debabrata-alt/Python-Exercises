# Find the maximum and minimum sized element in a list.

list = ["apple", "strawberry", "pineapple", "lichi", "kiwi", "orange"]

def func_len(a):
  return len(a)

x = min(list, key=func_len)

print(x) # kiwi

y = max(list, key=func_len)

print(y) # strawberry

#////////////////////////////////////////////////
# Using lambda function

list = ["apple", "strawberry", "pineapple", "lichi", "kiwi", "orange"]

x = min(list, key=lambda a: len(a))

print(x) # kiwi

y = max(list, key=lambda a: len(a))

print(y) # strawberry
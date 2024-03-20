# Write a Python program to find repeated items in a tuple.

tuplex = 2, 4, 5, 6, 2, 3, 4, 4, 7

mul_nums = tuple(el for el in tuplex if tuplex.count(el) > 1)

print(mul_nums) # (2, 4, 2, 4, 4)

print(set(mul_nums)) # {2, 4}

#///////////////////////////////////////////////////////////////////////////////////////

from collections import Counter

tuplex = 2, 4, 5, 6, 2, 3, 4, 4, 7

c_obj = Counter(tuplex)

print(c_obj)
# Counter({4: 3, 2: 2, 5: 1, 6: 1, 3: 1, 7: 1})

mul_nums = tuple(key for key, count in c_obj.items() if count > 1)

print(mul_nums) # (2, 4)
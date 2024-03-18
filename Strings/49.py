# Write a Python program to compute the sum of the digits in a given string.


def func(string): 
  l = [int(s) for s in string if s.isdigit()]
  return sum(l)

print(func("123abcd45")) # 15
print(func("abcd1234")) # 10
# Write a Python program to remove leading zeros from an IP address.


def func(string):
  listy = string.split(".")
  return ".".join(str(int(el)) for el in listy)


print(func("255.024.01.01")) # 255.24.1.1
print(func("127.0.0.01")) # 127.0.0.1
print(func("127.0.0.01.007.245.013")) # 127.0.0.1.7.245.13
print(func("127.007.2400.0013")) # 27.7.2400.13


#//////////////////////////////////////////
# NOTE
# An integer number do NOT start with leading zeros.

str = "007"
print(int(str)) # 7

str = "00015"
print(int(str)) # 15

str = "000150"
print(int(str)) # 150

str = "0001500"
print(int(str)) # 1500
# Write a Python program to find the maximum length of consecutive 0's in a given binary string.

def func(bin_string):
  return max(map(len, bin_string.split("1")))


print(func("111000010000110")) # 4
print(func("111000111")) # 3


#//////////////////////////////////////

# len() is a built in function. It returns the number of items in a container.
# len() => int

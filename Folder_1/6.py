# List of all Abundant nos - from 1 to 1000

num_list = []
sum = 0
for num in range(1, 1001):
  for n in range(1, num):
    if num % n == 0:
      sum += n
  if sum > num:
    num_list.append(num)
  sum = 0

# print(num_list)

all_abundant_nums = " ".join(str(num) for num in num_list)
print(f"All abundant numbers from 1 to 1000:\n{all_abundant_nums}")



# //////////////////////////////////////////////////////////////////////////////

# 1) 
# 8 ways to add an element to the beginning of a list and string in Python:
# https://dev.to/ra1nbow1/8-ways-to-add-an-element-to-the-beginning-of-a-list-and-string-in-python-925#:~:text=Method%201%3A%20insert&text=The%20insert()%20method%20takes,as%20the%20first%20parameter%201%20.

# 2)
# list = [1, 2, 3]
# print([4] + list) # [4, 1, 2, 3]


# 3)
# Python List to String – How to Convert Lists in Python:
# https://www.freecodecamp.org/news/python-list-to-string-how-to-convert-lists-in-python/


# 4) Python String split() Method:
# The split() method splits a string into a list. 
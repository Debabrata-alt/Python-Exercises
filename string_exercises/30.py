# Write a Python program to reverse a string.

string = "javascript"

reversed_object = reversed(string)

reversed_string = "".join(reversed_object)

print(reversed_string) # tpircsavaj

#/////////////////////////////////////////////////////

string = "javascript"

reversed_string = string[::-1]

print(reversed_string) # tpircsavaj


#/////////////////////////////////////////////////////

# NOTE:

# In Python, [::-1] is a slice that reverses a string or list. It can be used to reverse the order of the elements in a string or list.

# Reverse a string
string = "hello world"
reversed_string = string[::-1]
print(reversed_string) # dlrow olleh

# Reverse a list
list = [1, 2, 3, 4, 5]
reversed_list = list[::-1]
print(reversed_list) # [5, 4, 3, 2, 1]


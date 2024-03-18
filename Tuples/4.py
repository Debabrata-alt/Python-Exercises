#  Write a Python program to unpack a tuple into several variables.

# Create a tuple containing three numbers
tuplex = 4, 8, 3

print(tuplex) # (4, 8, 3) 

# Unpack the values from the tuple into the variables n1, n2, and n3
n1, n2, n3 = tuplex

print(n1 + n2 + n3) # 15

# Attempt to unpack the tuple into more variables (n1, n2, n3, and n4)
# This will raise a "ValueError" since there are not enough values in the tuple to unpack into all the variables
n1, n2, n3, n4 = tuplex

# Write a Python program to reverse a tuple.

# Create a tuple containing a single string
x = ("w3resource")

# Reverse the characters in the string by using the 'reversed' function.
y = reversed(x)

print(y) # <reversed object at 0x0000027457095A20>

# convert the reversed object back into a tuple and print it.
print(tuple(y))
# ('e', 'c', 'r', 'u', 'o', 's', 'e', 'r', '3', 'w')

# Create another tuple containing a sequence of numbers
x = (5, 10, 15, 20)

# Reverse the order of the elements in the tuple using the 'reversed' function.
y = reversed(x)

# convert the reversed object back into a tuple and print it.
print(tuple(y)) 
# (20, 15, 10, 5)

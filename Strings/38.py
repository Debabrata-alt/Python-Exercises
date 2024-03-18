# Write a Python program to swap commas and dots in a string.
# Sample string: "32.054,23"
# Expected Output: "32,054.23"

amount = "32.054,23"

# Create a variable 'maketrans' that references the 'maketrans' method of the 'amount' string.
maketrans = amount.maketrans

print(maketrans) # built-in method maketrans of type object at 0x00007FF931AF8F30>

# Translate (replace) the characters ',' with '.', and '.' with ',' in the 'amount' string using the 'maketrans' variable.
amount = amount.translate(maketrans(",.", ".,"))

# Print the modified 'amount' string with the swapped decimal and comma characters.
print(amount) # 32,054.23

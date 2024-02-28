# Write a Python program to format a number with a percentage.

x = 0.25
y = -0.25

# Format the value of 'x' as a percentage with two decimal places and print it.

print("{:.2%}".format(x)) # 25.00%

print(f"{x: .2%}") # 25.00%

# Format the value of 'y' as a percentage with two decimal places and print it.

print("{:.2%}".format(y)) # -25.00%

print(f"{y: .2%}") # -25.00%


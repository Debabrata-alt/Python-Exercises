# Python: Display a number with a comma separator.

x = 3000000
y = 30000000

# Format the value of 'x' with a comma separator for thousands and print it.

print(f"{x: ,}") # 3,000,000

# Format the value of 'y' with a comma separator for thousands and print it.

print(f"{y: ,}") # 30,000,000


#//////////////////////////////////////////////

# Another way with format() method:

print("{:,}".format(x)) # 3,000,000

print("{:,}".format(y)) # 30,000,000



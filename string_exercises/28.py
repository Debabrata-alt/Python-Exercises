# Write a Python program to print the following integers with zeros to the left of the specified width.

x = 3

# left padding

print("{:0>2d}".format(x)) # 03
print("{:0>3d}".format(x)) # 003
print("{:0>4d}".format(x)) # 0003

print("{:1>2d}".format(x)) # 13
print("{:1>3d}".format(x)) # 113
print("{:1>4d}".format(x)) # 1113

# right padding

print("{:0<2d}".format(x)) # 30
print("{:0<3d}".format(x)) # 300
print("{:0<4d}".format(x)) # 3000

print("{:1<2d}".format(x)) # 31
print("{:1<3d}".format(x)) # 311
print("{:1<4d}".format(x)) # 3111


#////////////////////////////////////////////////////////////////////////

# NOTE:
# 2d = total width of 2 characters.
# 0>2d = total width of 2 chartacters, spacings will be filled with 0s from the left.

# 3d = total width of 3 characters.
# 0>3d = total width of 3 chartacters, spacings will be filled with 0s from the left.

# 1>2d = total width of 2 chartacters, spacings will be filled with 1s from the left.

# 1>3d = total width of 3 chartacters, spacings will be filled with 1s from the left.

# 0<2d = total width of 2 chartacters, spacings will be filled with 0s from the right.

# 0<3d = total width of 3 chartacters, spacings will be filled with 0s from the right.

# 1<2d = total width of 2 chartacters, spacings will be filled with 1s from the right.

# 1<3d = total width of 3 chartacters, spacings will be filled with 1s from the right.



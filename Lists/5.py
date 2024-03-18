# Write a Python program to clone or copy a list.

# 1st method 

original_list = [10, 22, 44, 23, 4]

copy_list = list(original_list)

print(copy_list) # [10, 22, 44, 23, 4]

#//////////////////////////////

# 2nd method

copy_list = original_list[:]

print(copy_list) # [10, 22, 44, 23, 4]

#//////////////////////////////

# 3rd method

copy_list = original_list.copy()

print(copy_list) # [10, 22, 44, 23, 4]
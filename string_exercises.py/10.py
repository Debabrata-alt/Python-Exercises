# Write a Python program to change a given string to a newly string where the first and last chars have been exchanged.

string = input("Enter the string: ") # Debabrata

first_char = string[0]
last_char = string[-1]

# Reverse
first_char = string[-1]
last_char = string[0]

new_string = first_char + string[1: -1] + last_char

print(new_string) # aebabratD
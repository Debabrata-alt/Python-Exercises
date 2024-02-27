# Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
# Sample String : 'abc', 'xyz'
# Expected Result : 'xyc abz'

str1, str2  = input("Enter 2 strings: ").split() # abc, xyz

first_2_chars_str1 = str1[:2]
first_2_chars_str2 = str2[:2]

new_str1 = first_2_chars_str2 + str1[2:]
new_str2 = first_2_chars_str1 + str2[2:]

new_star = new_str1 + " " + new_str2

print(new_star) # xyc abz


# How to take Multiple Input from User in Python:
# https://www.javatpoint.com/how-to-take-multiple-input-from-user-in-python
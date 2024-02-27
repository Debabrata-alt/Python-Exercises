# Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
# Sample String : 'restart'
# Expected Result : 'resta$t'

my_str = input("Enter the string: ") 
# Restarters | restarters | Avantibabamandal | avantibabamandal
first_char = my_str[0]
new_first_char = ""

if first_char.isupper():
  new_first_char = first_char.lower()
else:
  new_first_char = first_char

new_str = my_str[1:]

new_str = new_str.replace(new_first_char, "$")

print(f"{new_first_char if first_char.islower() else first_char}" + new_str) 
# Resta$te$s| resta$te$s | Av$ntib$b$m$nd$l | av$ntib$b$m$nd$l
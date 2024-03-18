# Write a Python program to remove characters that have odd index values in a given string.

str = input("Enter the string: ") # Avantika
new_str = ""

for n in range(len(str)):
  if n % 2 == 0:
    new_str += ""
  else:
    new_str += str[n]

print(str[0] + new_str) # Avnia


# 0 / 2 = 0, there is no remainder. thus 0 % 2 = 0
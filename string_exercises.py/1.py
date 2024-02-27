# Write a Python program to count the number of characters (character frequency) in a string.
# Sample String : google.com'
# Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}

string = input("Enter the string: ")  # google.com
frequency_dict = {}

for char in string:
  count = string.count(char)
  frequency_dict[char] = count

print(frequency_dict) 
# {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}

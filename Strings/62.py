# Write a Python program to count Uppercase, Lowercase, special characters and numeric values in a given string.


# Function to count character types
def count_chars(str):
  # Initialize counters
  upper_ctr, lower_ctr, number_ctr, special_ctr = 0, 0, 0, 0
  # Iterate through string
  for i in range(len(str)):
    # Increment appropriate counter 
    if str[i] >= 'A' and str[i] <= 'Z':
      upper_ctr += 1
    elif str[i] >= 'a' and str[i] <= 'z':
      lower_ctr += 1
    elif str[i] >= '0' and str[i] <= '9':
      number_ctr += 1
    else:
      special_ctr += 1

  return upper_ctr, lower_ctr, number_ctr, special_ctr


u, l, n, s = count_chars("@W3Resource.Com")


print(f'Upper case characters: {u}') # Upper case characters: 3
print(f'Lower case characters: {l}') # Lower case characters: 9
print(f'Number case: {n}') # Number case: 1
print(f'Special case characters: {s}') # Special case characters: 2


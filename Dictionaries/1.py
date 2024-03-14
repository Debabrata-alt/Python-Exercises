# Write a Python script to add a key to a dictionary.

# Sample Dictionary : {0: 10, 1: 20}
# Expected Result : {0: 10, 1: 20, 2: 30}

s_dict = {0: 10, 1: 20}

s_dict[2] = 30

print(s_dict)
# {0: 10, 1: 20, 2: 30}

s_dict.update({3: 40})

print(s_dict)
# {0: 10, 1: 20, 2: 30, 3: 40}
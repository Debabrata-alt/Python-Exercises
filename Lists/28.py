# Write a Python program to flatten a given nested list structure.
# Original list: [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
# Flatten list:
# [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]


def flatten_list(input_list):
  # Initialize an empty list 'result_list' to store the flattened elements
  result_list = []

  # Check if 'input_list' is empty; if so, return an empty result list
  if not input_list:
    return result_list

  # Create a stack to keep track of nested lists; start with 'input_list' as the initial item in the stack
  stack = [list(input_list)]

  # Iterate while the stack is not empty
  while stack:
    # Pop the current list 'c_num' from the stack
    c_num = stack.pop()

    # Pop the next item from 'c_num'
    next = c_num.pop()

    # If 'c_num' is not empty, push it back onto the stack
    if c_num:
      stack.append(c_num)

    # Check if 'next' is a list
    if isinstance(next, list):
      # If 'next' is a non-empty list, push it onto the stack
      if next:
        stack.append(list(next))
    else:
      # If 'next' is not a list, add it to 'result_list'
      result_list.append(next)

  # Reverse 'result_list' to maintain the original order of elements
  result_list.reverse()

  # Return the flattened list
  return result_list


# Define a nested list 
input_list = [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]

print(flatten_list(input_list)) 
# [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]

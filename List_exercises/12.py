# Write a Python program to generate all permutations of a list in Python.

# Import the 'itertools' module, which provides various functions for working with iterators
import itertools

# Use 'itertools.permutations' to generate all permutations of the list [1, 2, 3], and convert the result to a list
# This will produce all possible orderings of the elements in the list

permutation_obj = itertools.permutations([1, 2, 3])

permutation_list = list(permutation_obj)

print(permutation_list)
# [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]

#////////////////////////////////////////////////////////////////////////

permutation_obj = itertools.permutations([1, 2, 3], 2)

permutation_list = list(permutation_obj)

print(permutation_list)
# [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]
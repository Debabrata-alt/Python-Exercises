# Write a Python program to move all spaces to the front of a given string in a single traversal.

def func(string):
  string_without_spaces = "".join(s for s in string if s != " ")
  no_of_spaces = len(string) - len(string_without_spaces)
  return (" " * no_of_spaces) + string_without_spaces


print(func("Python  Exercises")) # "  PythonExercises"
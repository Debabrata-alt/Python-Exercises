# Write a Python program to insert space before every capital letter appears in a given word.
# Sample Data:
# ("PythonExercises") -> "Python Exercises"
# ("Python") -> "Python"
# (“PythonExercisesPracticeSolution”) -> “Python Exercises Practice Solution”


def func(word):
  result = ""
  for i in word:
    if i.isupper():
      result += " " + i.upper()
    else:
        result += i
  # Remove the leading whitespace from the result and return    
  return result[1:]


print(func("PythonExercises")) # Python Exercises
print(func("Python")) # Python
print(func("PythonExercisesPracticeSolution")) # Python Exercises Practice Solution
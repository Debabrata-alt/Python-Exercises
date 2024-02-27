# Write a Python function to get a string made of 4 copies of the last two characters of a specified string (length must be at least 2).
# Sample function and result :
# insert_end('Python') -> onononon
# insert_end('Exercises') -> eseseses

def insert_end(str):
  if len(str) < 2:
    return str
  else:
    return str[-2: ] * 4

copies = insert_end("Python")
print(copies) # onononon

copies = insert_end("Exercises")
print(copies) # eseseses
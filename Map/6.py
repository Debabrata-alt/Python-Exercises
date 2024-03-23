# Write a Python program to convert all the characters into uppercase and lowercase and eliminate duplicate letters from a given sequence. Use the map() function.

chars = {'a', 'b', 'E', 'f', 'a', 'i', 'o', 'U', 'a'}

def myFunc(char):
  return char.upper(), char.lower()

newChars = set(map(myFunc, chars))

print(newChars)
# {('A', 'a'), ('I', 'i'), ('F', 'f'), ('B', 'b'), ('E', 'e'), ('U', 'u'), ('O', 'o')}


# Write a Python program to scramble the letters of a string in a given list.

from random import shuffle

org_list = ['Python', 'list', 'exercises', 'practice', 'solution']

def scramble(input_list):
  new_list = []
  for el in input_list:
    char_list = list(el)
    shuffle(char_list)
    char_str = "".join(char_list)
    new_list.append(char_str)
  return new_list


print(scramble(org_list))
# ['onPhyt', 'itls', 'ercseeixs', 'peraictc', 'oltiosnu']

#//////////////////////////////////////////////////////////////////////////////////////////

# Does 'random.shuffle' work on strings?

# No, the random.shuffle() function in Python does not work on strings. This is because strings are immutable, meaning that their contents cannot be changed once they are created.
# To shuffle a string, you can convert it to a list of characters, shuffle the list using random.shuffle(), and then join the characters back into a string.

# Example:

from random import shuffle

string = "hello world"

characters = list(string)

print(characters) # ['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']

shuffle(characters)

shuffled_string = "".join(characters)

print(shuffled_string) # dlrow olleh

#//////////////////////////////////////////////////////////////////

from random import shuffle

my_str = "python"

my_list = list(my_str) 

print(my_list) # ['p', 'y', 't', 'h', 'o', 'n']

shuffle(my_list)

print(my_list) # ['n', 'h', 't', 'o', 'y', 'p']
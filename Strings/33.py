# Write a Python program to count repeated characters in a string.
# Sample string: 'thequickbrownfoxjumpsoverthelazydog'
# Expected output :
# o 4
# e 3
# u 2
# h 2
# r 2
# t 2

def count_repeated_chars(string):
  set = {(s, string.count(s)) for s in string if string.count(s) > 1}
  for s in set:
    print(s[0], s[1])


count_repeated_chars("thequickbrownfoxjumpsoverthelazydog")
# t 2
# o 4
# e 3
# u 2
# r 2
# h 2
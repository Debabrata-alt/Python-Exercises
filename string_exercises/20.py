# Write a Python program to remove a newline in Python.

s = "I am Raju\nI am 40 years old\nI live in Bankura\nMy wife is Pinku\nMy daughter is Avantika"

def remove_newlines(s):
  return s.replace("\n", "")


print(remove_newlines(s))
# I am RajuI am 40 years oldI live in BankuraMy wife is PinkuMy daughter is Avantika
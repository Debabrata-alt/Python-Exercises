# Write a Python program to create a Caesar encryption.

uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar_cipher(string, shift_no):
  new_string = ""
  if shift_no >= len(uppercase):
    shift_no %= len(uppercase)
  if shift_no >= len(lowercase):
    shift_no %= len(lowercase)
  for s in string:
    if s.isupper():
      i = uppercase.index(s)
      if i + shift_no >= len(uppercase):
        new_string += uppercase[(i + shift_no) % len(uppercase)]
      else: 
        new_string += uppercase[i + shift_no]
    elif s.islower():
      i = lowercase.index(s)
      if i + shift_no >= len(lowercase):
        new_string += lowercase[(i + shift_no) % len(lowercase)]
      else: 
        new_string += lowercase[i + shift_no]
    elif s.isdigit():
      new_string += str(int(s) + shift_no)
    else:
      new_string += s
  return new_string


print(caesar_cipher("AbcD123", 2)) # CdeF345
print(caesar_cipher("bcDE234", 3)) # efGH567
print(caesar_cipher("cdGH56", 4)) # ghKL910

print(caesar_cipher("uVWXyz", 6)) # aBCDef
print(caesar_cipher("pQRst", 12)) # bCDef

print(caesar_cipher("cdGHyZ", 28)) # efIJaB
print(caesar_cipher("ghiJK", 32)) # mnoPQ



# Write a Python program to reverse words in a string.

string = """
When I opened my phonepe account, a message flashed on the screen, saying that I had to pay Rs 1000 to an unknown account named JetPrivilege 
"""

def reversed_words(string):
  return " ".join(string.strip().split()[::-1])


print(reversed_words(string))

# JetPrivilege named account unknown an to 1000 Rs pay to had I that saying screen, the on flashed message a account, phonepe my opened I When


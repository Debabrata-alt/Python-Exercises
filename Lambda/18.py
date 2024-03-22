# Write a Python program to find palindromes in a given list of strings using Lambda.
# Orginal list of strings:
# ['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']
# List of palindromes:
# ['php', 'aaa']

myList = ['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']

palin_list = list(filter(lambda el: el == el[::-1], myList))

print(palin_list)
# ['php', 'aaa']

#////////////////////////////////////////////////////////////////////////////////////////////

myList = ['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']

palin_list = list(filter(lambda el: el == "".join(reversed(el)), myList))

print(palin_list)
# ['php', 'aaa']
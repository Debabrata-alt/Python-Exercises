
# Write a Python program to find all anagrams of a string in a given list of strings using Lambda.
# Orginal list of strings:
# ['bcda', 'abce', 'cbda', 'cbea', 'adcb']
# Anagrams of 'abcd' in the above string:
# ['bcda', 'cbda', 'adcb']

myList = ['bcda', 'abce', 'cbda', 'cbea', 'adcb', 'abcefghd', 'bcghad', 'cabd']

anagrams = list(filter(lambda el: all(e in "abcd" for e in el), myList))

print(anagrams)
# ['bcda', 'cbda', 'adcb', 'cabd']
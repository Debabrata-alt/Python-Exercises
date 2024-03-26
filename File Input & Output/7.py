# Write a python program to find the longest words.

with open("demo.txt", mode="r") as f:
  # f.read() is a single string. split the string into a list by the whitespace.
  # 'words' is now a list of all the words in the file content.
  words = f.read().split()
  longest_word = max(words, key=len)

print(longest_word)
# general-purpose,

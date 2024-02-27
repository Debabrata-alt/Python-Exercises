# Write a Python function that takes a list of words and return the longest word and the length of the longest one.
# Sample Output:
# Longest word: Exercises
# Length of the longest word: 9

# Raju, Pinku, Debabrata, Avanti 
list_of_words = input("Enter the words: ").split(", ")  
print(list_of_words) # ['Raju', 'Pinku', 'Debabrata', 'Avanti']

def word_size(list_of_words):
  longest_word = ""
  for word in list_of_words:
    len_of_word = len(word)
    if len_of_word > len(longest_word):
      longest_word = word
  return longest_word

longest_word = word_size(list_of_words)

print(f"The longest word: {longest_word}")  # The longest word: Debabrata
print(f"Length of the longest word: {len(longest_word)}")  # Length of the longest word: 9
# Write a Python program to count the occurrences of each word in a given sentence.

word_list = input("Write the sentence: ").split()
lowercase_word_list = []
repeat_words_list = []
count_list = []
check_list = []

for word in word_list:
  lowercase_word = word.lower()
  lowercase_word_list.append(lowercase_word)
  
for word in lowercase_word_list:
  count = lowercase_word_list.count(word)
  if count > 1:
    repeat_words_list.append(word)
    count_list.append(count)

for word in lowercase_word_list:
  if word not in check_list:
    if word in repeat_words_list:
      word_index = repeat_words_list.index(word)
      count = count_list[word_index]
      print(f"{word[0].upper() + word[1:]}: {count} occurances")
    else:
      print(f"{word[0].upper() + word[1:]}: 1 occurance")
  check_list.append(word)


# Write the sentence: My house and my son is good but my son is not so good in sports but sports is not so important yet my cousin is so good in cooking
# My: 4 occurances
# House: 1 occurance
# And: 1 occurance
# Son: 2 occurances
# Is: 4 occurances
# Good: 3 occurances
# But: 2 occurances
# Not: 2 occurances
# So: 3 occurances
# In: 2 occurances
# Sports: 2 occurances
# Important: 1 occurance
# Yet: 1 occurance
# Cousin: 1 occurance
# Cooking: 1 occurance
  


# Write a Python program to find the second most repeated word in a given string.

unique_list = []

def sort_list(el):
  return el["count"]


def func(string):
  trans_string = string.translate(string.maketrans(".,", "  "))
  repeat_words_list_of_dicts = [{"word": s, "count": trans_string.split().count(s)} for s in trans_string.split() if trans_string.split().count(s) > 1]

  for el in repeat_words_list_of_dicts: 
    if el not in unique_list:
      unique_list.append(el)
    
  unique_list.sort(reverse=True, key=sort_list)
  
  if len(unique_list) > 1:
    return f"Second most repeated word is <{unique_list[1]["word"]}> with {unique_list[1]["count"]} occurances"  
  elif len(unique_list) == 1:
    return f"No Second most repeated word. The only repeated word is <{unique_list[0]["word"]}> with {unique_list[0]["count"]} occurances"
  else:
    return None


print(func("I felt happy because I saw the others were happy and because I knew I should feel happy, but I wasn't really happy."))


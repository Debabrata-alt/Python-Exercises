# Write a Python program to find the maximum number of characters (maximum occuring characters) in a given string.

def func(string):
  
  count_list = []
  
  list_of_dicts = [{"char" : s, "count": string.count(s)} for s in string]
  
  for el in list_of_dicts:
    count_list.append(el["count"])
    
  maxi = max(count_list)
  
  for el in list_of_dicts: 
    if maxi == el["count"]:
      return f"Max occuring char: {el["char"]}: {el["count"]} occurances" 


print(func("welcome to w3resource"))
# Max occuring char: e: 4 occurances

print(func("Python: Get file creation and modification date/times"))
# Max occuring char: t: 6 occurances

print(func("abcdefghijkb"))
# Max occuring char: b: 2 occurances

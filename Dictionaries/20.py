# Write a Python program to combine values in a list of dictionaries.
# Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
# Expected Output: Counter({'item1': 1150, 'item2': 300})

myList = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}, {'item': 'item1', 'amount': 550}, {'item': 'item2', 'amount': 850}, {'item': 'item3', 'amount': 450}]

newDict = {}

for el in myList:
  if el["item"] in newDict:
    newDict.update({el["item"]: newDict[el["item"]] + el["amount"]})
  else:
    newDict.update({el["item"]: el["amount"]})


print(newDict)
# {'item1': 1700, 'item2': 1150, 'item3': 450}

#//////////////////////////////////////////////////////////////////////////

from collections import Counter

item_list = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]

# Create an empty Counter object 'result' to store the summed amounts for each 'item'.
result = Counter()

for d in item_list:
  # Update the 'result' Counter by adding the 'amount' to the corresponding 'item' key.
  result[d['item']] += d['amount']


print(result)
# Counter({'item1': 1150, 'item2': 300})







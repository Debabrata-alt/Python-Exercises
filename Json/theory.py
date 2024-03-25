# json is used for encoding objects or other complex data structures as a string. 
import json

# JSON is a syntax for storing and exchanging data.
# JSON is text, written with JavaScript object notation.

#//////////////////////////////////////////////////////////////

# Parse JSON - Convert from JSON to Python object:
# If you have a JSON string, you can parse it by using the json.loads() method.

# Convert from JSON to Python:

# some JSON:
x = '{"name": "John", "age": 30, "city": "New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary.
print(y)
# {"name": "John", "age": 30, "city": "New York"}

print(y["age"]) # 30

#//////////////////////////////////////////////////////////////

# Convert from Python object to JSON
# If you have a Python object, you can convert it into a JSON string by using the json.dumps() method.

# Convert from Python to JSON:

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)
# "{"name": "John", "age": 30, "city": "New York"}"

#//////////////////////////////////////////////////////////////

# You can convert Python objects of the following types, into JSON strings:

# dict
# list
# tuple
# string
# int
# float
# True
# False
# None

print(json.dumps({"name": "John", "age": 30}))
# "{"name": "John", "age": 30}"

print(json.dumps(["apple", "bananas"]))
# "["apple", "bananas"]"

print(json.dumps(("apple", "bananas")))
# "["apple", "bananas"]"

print(json.dumps("hello"))
# "hello"

print(json.dumps(42))
# "42"

print(json.dumps(31.76))
# "31.76"

print(json.dumps(True))
# "true"

print(json.dumps(False))
# "false"

print(json.dumps(None))
# "null"

#//////////////////////////////////////////////////////////////

# When you convert from Python to JSON, Python objects are converted into the JSON (JavaScript) equivalent.

# Python	  JSON
# dict	   Object
# list	   Array
# tuple	   Array
# str	     String
# int	     Number
# float	   Number
# True	   true
# False	   false
# None	   null

#//////////////////////////////////////////////////////////////

# Convert a Python object containing all the legal data types:

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string.
print(y)
# "{"name": "John", "age": 30, "married": true, "divorced": false, "children": ["Ann","Billy"], "pets": null, "cars": [{"model": "BMW 230", "mpg": 27.5}, {"model": "Ford Edge", "mpg": 24.1}]}"

#//////////////////////////////////////////////////////////////

# Format the Result:

# The example above prints a JSON string, but it is not very easy to read, with no indentations and line breaks.

# The json.dumps() method has parameters to make it easier to read the result.  

#///////////////////////////////////////////////////

# 1. Use the indent parameter to define the numbers of indents:

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# use four indents to make it easier to read the result:
print(json.dumps(x, indent = 4))

# {
#     "name": "John",
#     "age": 30,
#     "married": true,
#     "divorced": false,
#     "children": [
#         "Ann",
#         "Billy"
#     ],
#     "pets": null,
#     "cars": [
#         {
#             "model": "BMW 230",
#             "mpg": 27.5
#         },
#         {
#             "model": "Ford Edge",
#             "mpg": 24.1
#         }
#     ]
# }

#/////////////////////////////////////////////////////////

# You can also define the separators, default value is (", ", ": "), which means using a comma and a space (", ") to separate each object, and a colon and a space (": ") to separate keys from values.

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# use . and a space to separate objects; 
# and a space, a = and a space to separate keys from their values.
print(json.dumps(x, indent = 4, separators = (". ", " = ")))

# {
#     "name" = "John".
#     "age" = 30.
#     "married" = true.
#     "divorced" = false.
#     "children" = [
#         "Ann".
#         "Billy"
#     ].
#     "pets" = null.
#     "cars" = [
#         {
#             "model" = "BMW 230".
#             "mpg" = 27.5
#         }.
#         {
#             "model" = "Ford Edge".
#             "mpg" = 24.1
#         }
#     ]
# }

#/////////////////////////////////////////////////////////

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# use a "<>" to separate objects; 
# and a space, a "~" and a space to separate keys from their values.
print(json.dumps(x, indent = 4, separators = ("<>", " ~ ")))

# {
#     "name" ~ "John"<>
#     "age" ~ 30<>
#     "married" ~ true<>
#     "divorced" ~ false<>
#     "children" ~ [
#         "Ann"<>
#         "Billy"
#     ]<>
#     "pets" ~ null<>
#     "cars" ~ [
#         {
#             "model" ~ "BMW 230"<>
#             "mpg" ~ 27.5
#         }<>
#         {
#             "model" ~ "Ford Edge"<>
#             "mpg" ~ 24.1
#         }
#     ]
# }

#/////////////////////////////////////////////////////////////////

# Order the Result:

# The json.dumps() method has parameters to order the keys in the result.

# Use the sort_keys parameter to specify if the result should be sorted or not:

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# sort the result alphabetically by keys:
print(json.dumps(x, indent = 4, sort_keys = True))

# {
#     "age": 30,
#     "cars": [
#         {
#             "model": "BMW 230",
#             "mpg": 27.5
#         },
#         {
#             "model": "Ford Edge",
#             "mpg": 24.1
#         }
#     ],
#     "children": [
#         "Ann",
#         "Billy"
#     ],
#     "divorced": false,
#     "married": true,
#     "name": "John",
#     "pets": null
# }


#///////////////////////////////////////////////////////////////////////////////////////////

# 'block in a dictionary. Here  we use json package to convert a dictionary to a string.
block = {"Raju": 40, "Pinku": 32}

# dumps() method creates json format strings from a object.
json.dumps(block)

# In our hash_block() function, we convert a block to a string. However, since a block is a dictionary, the order of its key value pairs are not guaranteed. And if for some reason (for example, a change in Python's memory optimization) its key value pairs switched position, then it will be treated as a different string (although it remains the the same dictionary with the same data in it).
# So, how to fix this problem? Well, Json.dumps() has a couple of named arguments and one of them is 'sort_keys'. We can set it to 'True'. Then it will sort the keys of the block (which is a dictionary) before making/dumping it to a string. that means the same dictionary will always lead to the same string, even if for some reason the order of its key-value pairs got changed.

def hash_block(block):
  return json.dumps(block, sort_keys = True)

# json.loads() takes a string in Json format and converts it back into native python Lists and objects.
# NOTE: 'file_content' is a List. 
# so, file_content[:-1] means the entite 'file_content' List except the last element.

file_content = ["...", "....", "..."]

blockchain = json.loads(file_content[:-1])




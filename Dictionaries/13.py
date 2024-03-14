# Write a Python program to get a dictionary from an object's fields.


# Define a class 'dictObj' that inherits from the 'object' class.
class dictObj(object):
  # Define the constructor method '__init__' for initializing object attributes.
  def __init__(self):
    # Initialize attributes 'x', 'y', and 'z' with string values.
    self.x = 'red'
    self.y = 'Yellow'
    self.z = 'Green'
  
  # Define a method 'do_nothing' that doesn't perform any actions (placeholder).
  def do_nothing(self):
    pass

# Create an instance 'test' of the 'dictObj' class.
test = dictObj()

# Print the '__dict__' attribute of the 'test' object, which contains its attribute-value pairs.
print(test.__dict__) 
# {'x': 'red', 'y': 'Yellow', 'z': 'Green'}

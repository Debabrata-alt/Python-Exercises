# Write a Python program to detect the number of local variables declared in a function.
# Sample Output:
# 3

# Define a function named 'abc'
def abc():
    # Define and assign values to local variables 'x', 'y', and 'str1' inside the function 'abc'
    x = 1
    y = 2
    str1 = "w3resource"
    
    # Print the string "Python Exercises"
    print("Python Exercises")

# Access the number of local variables in the function 'abc' using the __code__.co_nlocals attribute
print(abc.__code__.co_nlocals) # 3

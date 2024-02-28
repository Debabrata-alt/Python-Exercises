#  Write a Python function to reverse a string if its length is a multiple of 4.

def reverse(str):
  return "".join(reversed(str)) if len(str) % 4 == 0 else str


print(reverse("Rajubhai")) # iahbujaR
print(reverse("Rajuda")) # Rajuda

print(reverse("Raju1234")) # 4321ujaR
print(reverse("Raju12")) # Raju12



#/////////////////////////////////////////////////////

# NOTE: reversed() gives us a reversed object.

# alph = ["a", "b", "c", "d"]

# ralph = reversed(alph)

# print(ralph) # <reversed object at 0x00000253F6605BA0>
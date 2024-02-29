# Write a Python program to print the square and cube symbols in the area of a rectangle and the volume of a cylinder.
# Sample output:
# The area of the rectangle is 1256.66cm2
# The volume of the cylinder is 1254.725cm3


def calculate(l, b, r, h):
  area_rect = l * b
  vol_cylin = 3.14159 * (r ** 2) * h 
  return f"Area of rectange = {area_rect} cm\u00b2", f"Volume of cylinder = {vol_cylin} cm\u00b3"


print(calculate(l = 12, b = 6, r = 3, h = 10))
# ('Area of rectange = 72 cm²', 'Volume of cylinder = 282.7431 cm³')

tuple = calculate(l = 12, b = 6, r = 3, h = 10)

print(tuple[0], "\n", tuple[1])
# Area of rectange = 72 cm² 
#  Volume of cylinder = 282.7431 cm³



#///////////////

print('\u03C0') # π
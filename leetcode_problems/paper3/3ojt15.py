# 15.Write a function get_hypotenuse that returns the hypotenuse of a right triangle given 
# the other two sides.
# >>> get_hypotenuse(0, 0)
# 0.0
import math
def get_hypotenuse(x,y):
    return math.sqrt((x**2)+(y**2))
    # OR>> return ((x**2)+(y**2))**0.5
print(get_hypotenuse(3,4))
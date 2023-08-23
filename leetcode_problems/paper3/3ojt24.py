# 24.Write a class that represents a circle.The circle should have a radius, a diameter, 
# and an area. It should also have a nice string representation.

import math

class circle:

    def __init__(self,r):
        self.radius=r
        self.diameter=2*r
        self.area= math.pi*r**2

    def __str__(self):
        return f'The radius of circle is {self.radius},Diameter is {self.diameter},And area is {self.area}'        

c=circle(5)
print(c)
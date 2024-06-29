import math
class circle:
    def __init__(self,radius):
        self.radius=radius
        
    def calculat_area(self):
        return math.pi*self.radius**2
    
    
    def calculate_perimeter(self):
        return 2*math.pi*self.radius
    
    
radius=float(input("enter the radius"))
circle=circle(radius)
area= circle.calculat_area()
perimeter=circle.calculate_perimeter()

print(area)
print(perimeter)
    
    
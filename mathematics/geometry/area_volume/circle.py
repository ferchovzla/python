import math
from geometric_shape import GeometricShape

class Circle(GeometricShape):
   def __init__(self, radius=0.00):
	  self.name = "CIRCLE"
	  self.radius = radius
	  self.calculate_area()
	  self.calculate_perimeter()

   """ Function calculate Circle area.
       return float
   """
   def calculate_area(self):
      self.area = math.pi*self.radius**2
    
   """ Function calculate Circle perimeter.
       return float
   """
   def calculate_perimeter(self):
      self.perimeter = 2*math.pi*self.radius
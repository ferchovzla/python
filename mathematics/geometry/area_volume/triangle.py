import math
from geometric_shape import GeometricShape

class Triangle(GeometricShape):
   def __init__(self, base=0.00, height=0.00, side_a=0.00, side_b=0.00):
      self.name = "TRIANGLE"
      self.base = base
      self.height = height
      self.side_a = side_a
      self.side_b = side_b
      self.calculate_area()
      self.calculate_perimeter()

   """ Function calculate Triangle area.
       return float
   """
   def calculate_area(self):
      self.area = (self.base*self.height)/2
    
   """ Function calculate Triangle perimeter.
       return float
   """
   def calculate_perimeter(self):
      self.perimeter = self.base + self.side_a +self.side_b
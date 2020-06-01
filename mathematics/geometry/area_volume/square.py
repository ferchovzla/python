import math
from geometric_shape import GeometricShape

class Square(GeometricShape):
   def __init__(self, lenght, width=0):
    if not width:
	     self.name = "SQUARE"
    else:
       self.name = "RECTANGLE"
       self.width = width

    self.lenght = lenght
    self.calculate_area()
    self.calculate_perimeter()

   """ Function calculate Square area.
       return float
   """
   def calculate_area(self):
      if self.name == "SQUARE":
         self.area = self.lenght**2
      else:
         self.area = self.lenght*self.width 
      
   """ Function calculate Square perimeter.
       return float
   """
   def calculate_perimeter(self):
      if self.name == "SQUARE":
         self.perimeter = 4*self.lenght
      else:
         self.perimeter = 2*(self.lenght+self.width) 

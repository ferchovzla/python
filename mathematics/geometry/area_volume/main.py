from circle import Circle
from square import Square
from triangle import Triangle

print("***Calcular area, perimetro del Circulo ***\n")
radius=float(input("Ingrese el valor del radio del circulo: "))

myCircle = Circle(radius)

print("Area = "+str(myCircle.area))
print("Perimetro = "+str(myCircle.perimeter)+"\n")

print("***Calcular area, perimetro del Cuadrado ***\n")
lenght=float(input("Ingrese el valor del lado del cuadrado: "))

mySquare = Square(lenght)
print("Area = "+str(mySquare.area))
print("Perimetro = "+str(mySquare.perimeter)+"\n")

print("***Calcular area, perimetro del Rectangulo ***\n")
lenght=float(input("Ingrese el valor del largo del rectangulo: "))
width=float(input("Ingrese el valor del ancho del rectangulo: "))

myRectangle = Square(lenght, width)
print("Area = "+str(myRectangle.area))
print("Perimetro = "+str(myRectangle.perimeter)+"\n")

print("***Calcular area, perimetro del Triangulo ***\n")
lenght_side_a=float(input("Ingrese el valor del lado A del triangulo: "))
lenght_side_b=float(input("Ingrese el valor del lado B del triangulo: "))
base=float(input("Ingrese el valor de la base del triangulo: "))
height=float(input("Ingrese el valor de la altura del triangulo: "))

myTriangle = Triangle(base, height, lenght_side_a, lenght_side_b)
print("Area = "+str(myTriangle.area))
print("Perimetro = "+str(myTriangle.perimeter)+"\n")
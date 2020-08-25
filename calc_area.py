							# CALCULATOR OF AREA OF SQARE AND RECTANGLE #

print("shape is square and rectangle only")

shape = input("Which shape: ")
unit = input("Enter the unit: ")
Length = int(input("Enter the length: "))
Breadth = int(input("Enter the bredth: "))
Base = int(input("Enter the base: "))
Height =  int(input("Enter the height: "))


if shape == "square":
	AREA = Length * Length
	print("Area of the",shape,"is",AREA,"sq",unit)

if shape == "rectangle":
	area = Length * Breadth
	print("Area of the",shape,"is",area,"sq",unit)

if shape == "triangle":
	Area = 1/2 * Base * Height
	print("Area of the",shape,"is",Area,"sq",unit)

else:
	print("invalid input")









 

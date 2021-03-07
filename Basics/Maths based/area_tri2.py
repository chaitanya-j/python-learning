								# AREA OF TRIANGLE # 
Base = int(input("enter the base:"))
Height = int(input("enter the height:"))
Unit = input("enter the unit:")


AREA = 1/2 * Base * Height



if Unit == "mt":
	unit = AREA * 100
	print("area of triangle is",unit,"sq cm")

if Unit == "km":
	uniT = AREA * 1000
	print("area of triangle is",uniT,"sq cm")

else:
	print("INVALID INPUT.PLEASE TRY AGAIN")




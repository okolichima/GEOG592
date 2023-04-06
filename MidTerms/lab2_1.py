#Sample Solution for lab2 question 1
import math
radius = float(raw_input("Please input the radius of a circle\n"))

area = math.pi * radius**2
perimeter = 2*math.pi*radius

print("The circle's area is %s, and perimeter is %s." %(area, perimeter))

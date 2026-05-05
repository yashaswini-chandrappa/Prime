'''Take the radius (r) as user input and print the area.
Use the formula: Area = π * r2 (value of π = 3.14)'''

radius = int(input("Enter the radius : "))
pi = 3.14
area_of_circle = pi * (radius**2)
print(f"The area of a circle with radius {radius} is {area_of_circle}")
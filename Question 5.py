# Given Radius of circle is 30 meters.
from math import pi                                       # Importing pi from math module
r = 30                                                    # Given Radius 30
area_of_circle =pi*r**2                                   # Finding Area Of Circle
print(" Area of circle the with radius 30 is " + str(area_of_circle))       # Printing area of circle


circum_of_circle = 2*pi*r                                  # Finding circumference of circle
print(" Circumference of circle with the radius 30 is "  + str(circum_of_circle))           # Printing circumference of circle

radius = float(input("Enter the radius of circle"))              # Taking radius as input from user
area_of_circle_new_radius = pi*radius**2                         # Finding the area of circle using radius from user input
print(" Area of circle with radius" + str(radius) + "is"  + str(area_of_circle_new_radius))         # Printing the area of circle

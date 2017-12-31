""" This script contains functions with multiple parameters"""

def area_triangle(b, h):
    """ This function calculate the area of a circle with a given base = b and height = h"""
    return 0.5 * b * h

base = int(input("Enter the base :"))
height = int(input("Enter the height:"))
calc_area = area_triangle(base,height)
print(f"The Area of the triangle is: {calc_area}")

"""This script contains functions with a parameter"""

import math
def volume_sphere(r):
    """This function calculates the volume of a sphere with a given radius (r)"""
    return 4/3 * math.pi * r ** 3


radius = int(input("Enter the radius:"))
calc_radius = volume_sphere(radius)
print(f"The Volume of sphere with radius({radius}) is: {calc_radius}")

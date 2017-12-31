""" this script contains functions with default arguments """

def cm_convert(feet=0, inches=0):
    """ This function converts feet and inches to cms """
    feet_to_cm = feet * 12 * 2.54
    inch_to_cm = inches * 2.54
    return feet_to_cm + inch_to_cm

# Convert 5 feet to cm
print(f"Convert 5 feet to cm(s): {cm_convert(feet=5)}")

# Convert 20 inches to cm
print(f"Convert 20 inches to cm(s): {cm_convert(inches=20)}")

# Convert 5 feet 3 inches to cm
print(f"Convert 5 feet 3 inches to cm(s): {cm_convert(feet=5, inches=3)}")

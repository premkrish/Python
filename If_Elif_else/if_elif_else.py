# Check if a triangle is scalene, isoceles or equilateral
# A triangle is scalene, if all three sides are different
# A triangle is Isosceles if two sides are equal
# A ttriangle is equilateral, if all 3 sides are equal

a = int(input("Enter side a:"))
b = int(input("Enter side b:"))
c = int(input("Enter side c:"))

if a != b and b != c and c != a:
    print("This is a Scalene triangle")
elif a == b and b == c:
    print("This is an Equilateral triangle")
else:
    print("This is an Isosceles triangle")
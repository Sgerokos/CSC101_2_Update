# This program takes the length of three sides of a triangle as input and calculates the perimeter of the triangle.

import sys

def check_triangle_inequality(side1, side2, side3):
    if side1 + side2 <= side3 or side1 + side3 <= side2 or side2 + side3 <= side1:
        print("Two sides are less than the third. Please try again.")
        sys.exit()

# Ask the user to input the length of each side of the triangle
side1 = float(input("Please enter the length of the first side of the triangle: "))
side2 = float(input("Please enter the length of the second side of the triangle: "))
side3 = float(input("Please enter the length of the third side of the triangle: "))

# Check if the input satisfies the triangle inequality theorem
check_triangle_inequality(side1, side2, side3)

# Calculate the perimeter of the triangle and display the result
perimeter = side1 + side2 + side3
print("The perimeter of the triangle is", perimeter)
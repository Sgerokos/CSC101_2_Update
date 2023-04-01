# Imports the turtle module in python
import turtle

# Dictionary mapping spectral range to color
colors = {
    (380, 450): "violet",
    (450, 485): "blue",
    (485, 500): "cyan",
    (500, 565): "green",
    (565, 590): "yellow",
    (590, 625): "orange",
    (625, 700): "red"
}

# Input validation using a while loop
while True:
    spectral = int(input("Please Enter a Spectral Color in Wavelength "
                         "nano-meters (nm) Ranging From 380-700: "))
    if 380 <= spectral <= 700:
        break
    print("Invalid input. Please enter a number between 380 and 700.")

# Find the corresponding color and print it
for (start, end), color in colors.items():
    if start <= spectral <= end:
        print(f"The Color is {color.capitalize()}")
        turtle.color(color)
        style = ("Courier", 90, "italic")
        turtle.write(color.capitalize(), font=style, align="center")
        break

# If the number is not in the range of 380 - 700 an error message will print out
else:
    print("The Input You Have Entered is Not Recognized. "
          "\nPlease Input a Number Ranging From 380 - 700. Thank You!!!")
# Imports the turtle module in python
import turtle

def display_color(spectral):
    # Display the color name and draw the text with the corresponding color
    if 380 <= spectral < 450:
        print("The color is Violet")
        turtle.color("violet")
    elif 450 < spectral < 485:
        print("The color is Blue")
        turtle.color("blue")
    elif 485 < spectral < 500:
        print("The color is Cyan")
        turtle.color("cyan")
    elif 500 < spectral < 565:
        print("The color is Green")
        turtle.color("green")
    elif 565 < spectral < 590:
        print("The color is Yellow")
        turtle.color("yellow")
    elif 590 < spectral < 625:
        print("The color is Orange")
        turtle.color("orange")
    elif 625 < spectral <= 700:
        print("The color is Red")
        turtle.color("red")
    
    style = ("Courier", 90, "italic")
    turtle.write(turtle.color()[0].capitalize(), font=style, align="center")
    turtle.done()

def main():
    spectral = int(input("Please enter a spectral color in wavelength"
                         " nanometers (nm) ranging from 380-700: ", ))
    
    if 380 <= spectral <= 700:
        display_color(spectral)
    else:
        print("The input you have entered is not recognized."
              "\nPlease input a number ranging from 380 - 700. Thank you!!!")

main()
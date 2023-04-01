# Imports turtle module
import turtle

# Displays the turtle window
turtle.showturtle()

# Sets the background color to darkred
turtle.bgcolor("darkred")

# Draws the letter S
turtle.pensize(8)
turtle.color("turquoise")
turtle.backward(50)
turtle.right(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(50)

# Moves the pen to the right of the letter S
turtle.penup()
turtle.goto(75, -50)
turtle.pendown()

# Draws the letter G
turtle.pensize(4)
turtle.color("midnightblue")
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(20)
turtle.right(90)
turtle.forward(15)
turtle.left(90 * 2)
turtle.forward(30)

# Moves the pen to the right of the letter G
turtle.penup()
turtle.goto(100, -50)
turtle.pendown()

# Draws a star
turtle.pensize(12)
turtle.color("darkslategray")
for i in range(5):
    turtle.forward(300)
    turtle.right(144)

# Moves the pen below the first star
turtle.penup()
turtle.goto(100, -100)
turtle.pendown()

# Draws a second star
turtle.pensize(12)
turtle.color("silver")
for i in range(5):
    turtle.forward(300)
    turtle.right(144)

# Closes the turtle window
turtle.done()
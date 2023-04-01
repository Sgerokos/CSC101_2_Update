# Imports turtle module
import turtle

# Setup the turtle
turtle.showturtle()
turtle.shape("turtle")
turtle.pencolor('green')

def draw_polygon(sides, length, angle):
    for _ in range(sides):
        turtle.forward(length)
        turtle.left(angle)

# Draw a green star-like shape
draw_polygon(13, 200, 150)

# Set the background color
turtle.bgcolor("darkred")

# Draw a turquoise letter 'S'
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

# Move the turtle next to the letter 'S'
turtle.penup()
turtle.goto(75, -50)
turtle.pendown()

# Draw a midnight blue letter 'G'
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
turtle.left(180)
turtle.forward(30)

# Move the turtle to a new position
turtle.penup()
turtle.goto(100, -50)
turtle.pendown()
turtle.left(100)

# Draw a dark slate gray star
turtle.pensize(12)
turtle.color("darkslategray")
draw_polygon(5, 300, 144)

# Move the turtle to a new position
turtle.penup()
turtle.goto(100, -100)
turtle.pendown()
turtle.left(100)

# Draw a silver star
turtle.pensize(12)
turtle.color("silver")
draw_polygon(5, 300, 144)

# Draw a second silver star
turtle.pensize(12)
turtle.color("silver")
draw_polygon(5, 300, 144)

turtle.done()
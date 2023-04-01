import turtle

turtle.showturtle()

# Designing the letter S
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

# Drawing the letter G
turtle.penup()
turtle.goto(75, -50)
turtle.pendown()

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

turtle.done()
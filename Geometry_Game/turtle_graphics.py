import turtle

# Making an object of the class Turtle from turtle library
myturtle = turtle.Turtle()

# Start the turtle movement from certain coordinate and not drawing a line while moving (pen up)
myturtle.penup()
myturtle.goto(50, 75)

# Draw line while moving
myturtle.pendown()
myturtle.forward(100)  # moved forward 100 pixels
myturtle.left(90)  # turned 90 degrees
myturtle.forward(200)
myturtle.left(90)
myturtle.forward(100)
myturtle.left(90)
myturtle.forward(200)
turtle.done()
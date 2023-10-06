from random import randint
import turtle


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def falls_in_rectangle(self, gui_rect):
        if gui_rect.point1.x < self.x < gui_rect.point2.x and gui_rect.point1.y < self.y < gui_rect.point2.y:
            return True
        else:
            return False


class Rectangle:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def area(self):
        return (self.point2.x - self.point1.x) * (self.point2.y - self.point1.y)


class GuiRectangle(Rectangle):
    def draw(self, canvas):
        myturtle.penup()
        myturtle.goto(self.point1.x, self.point1.y)

        # Draw line while moving
        canvas.pendown()
        canvas.forward(self.point2.x - self.point1.x)  # moved forward 100 pixels
        canvas.left(90)  # turned 90 degrees
        canvas.forward(self.point2.y - self.point1.y)
        canvas.left(90)
        canvas.forward(self.point2.x - self.point1.x)
        canvas.left(90)
        canvas.forward(self.point2.y - self.point1.y)


class GuiPoint(Point):
    def draw(self, canvas, size=5, color='red'):
        canvas.penup()
        canvas.goto(self.x, self.y)
        canvas.pendown()
        canvas.dot(size, color)


gui_rect = GuiRectangle(Point(randint(0, 400), randint(0, 400)), Point(randint(10, 400), randint(10, 400)))

# Print rectangle co-ordinates
print("Rectangle co-ordinates are: ", gui_rect.point1.x, ", ", gui_rect.point1.y, "and ", gui_rect.point2.x, ", ",
      gui_rect.point2.y)

# Get Point and area from user

user_point = GuiPoint(float(input("Guess x: ")), float(input("Guess y: ")))
user_area = float(input("Guess rectangle area: "))

# Print the game results

print("Your area was inside rectangle : ", user_point.falls_in_rectangle(gui_rect))
print("Your are was off by: ", gui_rect.area() - user_area)

myturtle = turtle.Turtle()
gui_rect.draw(canvas=myturtle)

user_point.draw(canvas=myturtle)
turtle.done()

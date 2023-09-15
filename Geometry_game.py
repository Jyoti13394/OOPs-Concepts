import math
from random import randint

class Point:
    def __init__(self, x, y):
        print("Hey, I am an init method and I get executed automatically anytime an object is created of the class")
        self.x = x
        self.y = y

    def falls_in_rectangle(self, rect):
        print("I am an ordinary method which gets called only when I am called with an reference of the object of class")
        if rect.low_left.x < self.x < rect.up_right.x and rect.low_left.y < self.y < rect.up_right.y:
            return True
        else:
            return False

    def calc_distance(self, point):
        return math.sqrt((self.x - point.x)**2 + (self.y - point.y)**2)
class Rectangle:
    def __init__(self, low_left, up_right):
        self.low_left = low_left
        self.up_right = up_right


rect = Rectangle(Point(randint(0, 9), randint(0, 9)), Point(randint(10, 19), randint(10, 19)))
print("Rectangle cordinates are :", rect.low_left.x, ",", rect.low_left.y, ",", rect.up_right.x,",", rect.up_right.y)
user_point = Point(int(input("Guess X: ")), int(input("Guess Y: ")))
print(user_point.falls_in_rectangle(rect))
print("Distance between 2 points is: ", user_point.calc_distance(Point(5, 23)))

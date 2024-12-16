import turtle
import random
import math


class Sprite(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.speed(0)
        self.penup()


class Player(Sprite):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("player")
        self.score = 0


class Missile(Sprite):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.shapesize(0.3)
        self.speed = 1
        self.state = "ready"
        self.hideturtle()


class Ball(Sprite):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(0.7)
        self.speed = random.randint(1, 2)
        self.state = "ready"
        self.hideturtle()
        # Assign power based on color
        self.color(random.choice(["green", "blue", "yellow", "red"]))
        self.power = {
            "green": "increase_ball",
            "blue": "freeze",
            "yellow": "deflect",
            "red": "explode"
        }.get(self.color()[0], None)


def get_heading_to(t1, t2):  # Moved here to avoid circular import
    x1 = t1.xcor()
    y1 = t1.ycor()
    x2 = t2.xcor()
    y2 = t2.ycor()
    heading = math.atan2(y1 - y2, x1 - x2)
    heading = heading * 180.0 / 3.14159
    return heading


class Asteroid(Sprite):
    def __init__(self, player):
        super().__init__()
        self.color("brown")
        self.shape("asteroid")
        self.speed = random.randint(2, 3) / 50
        self.goto(0, 0)
        heading = random.randint(0, 260)
        distance = random.randint(300, 400)
        self.setheading(heading)
        self.fd(distance)
        self.setheading(get_heading_to(player, self))

import turtle
import random


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

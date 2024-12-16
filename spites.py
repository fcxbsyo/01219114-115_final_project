import turtle


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
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

import turtle

from sound_manager import SoundManager
import sprites
from score_manager import load_high_score, save_score


class Game:

    def __init__(self):
        self.wn = turtle.Screen()
        self.wn.setup(width=600, height=600)
        self.wn.title("Space Station Defense Game")
        self.wn.bgcolor("black")
        self.wn.bgpic("img/start_screen.gif")
        self.wn.tracer(0)

        self.sound_manager = SoundManager()
        self.register_shapes()

        self.player = sprites.Player()
        self.missiles = [sprites.Missile() for _ in range(3)]
        self.balls = [sprites.Ball() for _ in range(5)]
        self.asteroids = [sprites.Asteroid(self.player) for _ in range(5)]
        self.pen = self.create_pen()

        # Game state
        self.game_started = False
        self.game_paused = False
        self.game_over = False
        self.player_name = ""
        self.high_score = load_high_score()

        # Bind controls
        self.wn.onkey(self.start_game, "space")
        self.wn.onkey(self.show_instructions, "s")
        self.wn.listen()

    @staticmethod
    def create_pen():
        pen = sprites.Sprite()
        pen.color("white")
        pen.hideturtle()  # Hide the score initially
        pen.goto(0, 250)
        return pen

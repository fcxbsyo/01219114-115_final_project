import turtle
import random
import sys

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

    @staticmethod
    def set_asteroid_speed(ast):
        for asteroid in ast:
            asteroid.speed = random.randint(2, 3) / 50

    def register_shapes(self):
        player_vertices = ((0, 15), (-15, 0), (-18, 5), (-18, -5), (0, 0), (18, -5), (18, 5), (15, 0))
        asteroid_vertices = ((0, 10), (5, 7), (3, 3), (10, 0), (7, 4), (8, -6), (0, -10), (-5, -5), (-7, -7), (-10, 0),
                             (-5, 4), (-1, 8))
        self.wn.register_shape("player", player_vertices)
        self.wn.register_shape("asteroid", asteroid_vertices)

    def rotate_left(self):
        self.player.lt(20)

    def rotate_right(self):
        self.player.rt(20)

    def fire_missile(self):
        for missile in self.missiles:
            if missile.state == "ready":
                self.sound_manager.play_missile()
                missile.goto(0, 0)
                missile.showturtle()
                missile.setheading(self.player.heading())
                missile.state = "fire"
                break

    def activate_power(self, ball):
        power = ball.power
        if power == "increase_ball":
            for _ in range(3):
                new_ball = sprites.Ball()
                self.balls.append(new_ball)
        elif power == "freeze":
            for asteroid in self.asteroids:
                asteroid.speed = 0
            self.wn.ontimer(lambda: self.set_asteroid_speed(self.asteroids), 3000)
        elif power == "deflect":
            for missile in self.missiles:
                if missile.state == "fire":
                    missile.setheading(missile.heading() + 180)
        elif power == "explode":
            for asteroid in self.asteroids:
                if ball.distance(asteroid) < 50:
                    heading = random.randint(0, 260)
                    distance = random.randint(600, 800)
                    asteroid.setheading(heading)
                    asteroid.fd(distance)
                    asteroid.setheading(sprites.get_heading_to(self.player, asteroid))
                    asteroid.speed += 0.01
                    self.player.score += 10
                    self.pen.clear()
                    self.pen.write("Score: {}".format(self.player.score), False, align="center", font=(
                        "Monospace", 24, "normal"))
        ball.hideturtle()
        self.balls.remove(ball)

    def start_game(self):
        if not self.game_started or self.game_over:
            self.reset_game()
            self.player_name = turtle.textinput("Player Name", "Enter your name:")
            if self.player_name is None:
                self.player_name = "Unknown"
            self.game_started = True
            self.wn.listen()

        self.game_over = False
        self.game_paused = False
        self.wn.bgpic("img/background.gif")

        self.wn.onkeypress(self.rotate_left, "Left")
        self.wn.onkeypress(self.rotate_right, "Right")
        self.wn.onkeypress(self.fire_missile, "space")
        self.wn.onkey(self.pause_game, "Escape")

        self.sound_manager.play_click()
        self.game_loop()

    def pause_game(self):
        self.sound_manager.play_click()

        self.game_paused = True
        self.hide_game_objects()
        self.wn.update()

        self.pen.hideturtle()
        self.pen.clear()

        self.wn.bgpic("img/pause_screen.gif")
        self.wn.onkey(self.resume_game, "c")
        self.wn.onkey(self.reset_game, "r")
        self.wn.onkey(self.exit_game, "x")
        self.wn.listen()

    def resume_game(self):
        self.game_paused = False

        self.player.showturtle()
        self.pen.showturtle()
        self.pen.write("Score: {}".format(self.player.score), False, align="center", font=("Monospace", 24, "normal"))

        for missile in self.missiles:
            if missile.state == "fire":
                missile.showturtle()
        for ball in self.balls:
            if ball.state == "fire":
                ball.showturtle()
        for asteroid in self.asteroids:
            asteroid.showturtle()

        self.wn.bgpic("img/background.gif")
        self.wn.onkey(self.pause_game, "p")
        self.wn.onkey(None, "r")
        self.wn.onkey(None, "s")
        self.wn.onkey(None, "x")
        self.wn.update()
        self.wn.listen()

        self.update_positions()

    def reset_game(self):
        self.game_over = False
        self.game_paused = False
        self.wn.bgpic("img/background.gif")
        self.reset_game_objects()
        # Reset player
        self.player.goto(0, 0)
        self.player.showturtle()
        self.player.score = 0

        # Reset score
        self.pen.clear()
        self.pen.write("Score: 0", False, align="center", font=("Monospace", 24, "normal"))
        self.pen.goto(0, 250)

        self.sound_manager.play_click()
        # Resume game
        self.resume_game()

    def exit_game(self):
        self.wn.bye()
        sys.exit()

    def show_instructions(self):
        self.wn.bgpic("img/how_to_play_screen.gif")
        self.wn.onkey(self.go_back_from_instructions, "Escape")
        self.wn.listen()

    def go_back_from_instructions(self):
        self.wn.bgpic("img/start_screen.gif")
        self.wn.onkey(self.start_game, "space")
        self.wn.onkey(self.show_instructions, "s")
        self.wn.onkey(self.exit_game, "x")
        self.wn.listen()

    def go_back_to_start_screen(self):
        self.game_paused = False
        self.game_started = False
        self.game_over = False

        self.hide_game_objects()

        self.player.goto(0, 0)
        self.player.score = 0
        self.pen.clear()

        self.wn.bgpic("img/start_screen.gif")
        self.wn.onkey(self.start_game, "space")
        self.wn.onkey(self.show_instructions, "s")
        self.wn.onkey(self.go_back, "Escape")
        self.sound_manager.play_click()

        self.wn.listen()
        self.reset_game_objects()
        self.wn.update()

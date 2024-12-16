from game import Game

if __name__ == "__main__":
    game = Game()

    game.wn.onkey(game.start_game, "space")
    game.wn.onkey(game.show_instructions, "s")

    game.wn.listen()
    game.wn.mainloop()

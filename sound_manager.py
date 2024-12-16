import pygame


class SoundManager:
    def __init__(self):
        pygame.mixer.init()
        self.missile_sound = pygame.mixer.Sound("sound/missile.wav")
        self.explosion_sound = pygame.mixer.Sound("sound/explosion.wav")
        self.click_sound = pygame.mixer.Sound("sound/click.wav")
        self.power_up_sound = pygame.mixer.Sound("sound/powerup.wav")
        pygame.mixer.music.load("sound/background_music.mp3")
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.5)
        self.is_paused = False

    def play_missile(self):
        self.missile_sound.play()

    def play_explosion(self):
        self.explosion_sound.play()

    def play_click(self):
        if not self.is_paused:
            self.click_sound.play()

    def set_pause_state(self, is_paused):
        self.is_paused = is_paused

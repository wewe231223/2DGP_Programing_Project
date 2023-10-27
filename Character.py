from pico2d import *


class Character:
    def __init__(self):
        self.image = load_image("Resources/character_animations.png")
        self.action = 4
        self.width = 150
        self.height = 150
        self.x = 100
        self.y = 100
        self.action = 6
        self.frame = 0

    def render(self):
        self.image.clip_draw(self.frame * self.width, self.width * self.action, self.width, self.width, self.x, self.y,300,300)


    def update(self):
        self.frame = (self.frame+1) % 5
        delay(0.3)
        pass


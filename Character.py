from pico2d import *


class Character:
    def __init__(self):
        self.image = load_image("Resources/character_animations.png")
        self.action = 4
        self.width = 150
        self.height = 150
        self.x = 100
        self.y = 100

    def render(self):
        self.image.clip_draw(0,self.width,self.width,self.width,self.x,self.y)


    def update(self):
        pass


import math

from pico2d import load_image, draw_rectangle
from math import *


class BackGround:
    def __init__(self):
        self.image1 = load_image("Resources/BackGround_1/1.png")
        self.image2 = load_image("Resources/BackGround_1/2.png")
        self.image3 = load_image("Resources/BackGround_1/3.png")
        self.image4 = load_image("Resources/BackGround_1/4.png")
        self.image5 = load_image("Resources/BackGround_1/5.png")

        self.x = 0


    def render(self):
        # 산 부분
        self.image5.draw(960 + self.x, 540, 1920, 1080)
        self.image4.draw(960 + self.x, 540, 1920, 1080)

        # 도로 부분
        self.image3.composite_draw(0, '', 960 + self.x, 540, 1920, 1080)
        self.image2.composite_draw(0, '', 960 + self.x, 540, 1920, 1080)
        self.image1.composite_draw(0, '', 960 + self.x, 540, 1920, 1080)


        draw_rectangle(0, 0, 1920, 30)

        pass
    def update(self):
        self.x -= 1
        pass

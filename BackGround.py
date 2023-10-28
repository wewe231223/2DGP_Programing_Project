import math

from pico2d import load_image
from math import *


class BackGround:
    def __init__(self):
        self.image1 = load_image("Resources/BackGround_1/1.png")
        self.image2 = load_image("Resources/BackGround_1/2.png")
        self.image3 = load_image("Resources/BackGround_1/3.png")
        self.image4 = load_image("Resources/BackGround_1/4.png")
        self.image5 = load_image("Resources/BackGround_1/5.png")



    def render(self):
        # 산 부분
        self.image5.draw(960, 540, 1920, 1080)
        self.image4.draw(960, 540, 1920, 1080)

        # 도로 부분
        self.image3.composite_draw(-pi / 12, '', 960, 540, 1920, 1080)
        self.image2.composite_draw(-pi / 12, '', 960, 540, 1920, 1080)
        self.image1.composite_draw(-pi / 12, '', 960, 540, 1920, 1080)



        pass
    def update(self):

        pass

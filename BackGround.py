import math

from pico2d import load_image, draw_rectangle , get_canvas_width , get_canvas_height
from random import randint
import random

def CreateVelocity():
    result = random.sample(range(1, 100), 5)
    result.sort()
    floatresult = []
    for i in result:
        floatresult.append( float(i) / 10.0 )

    print(floatresult)
    return floatresult


BackSpeed = CreateVelocity()

class BackImage:
    def __init__(self,depth,position = 1):
        self.image = load_image("./Resources/BackGround_1/"+"%d"%(5-depth)+".png")
        self.x = (get_canvas_width() / 2) * (position * 2 - 1)
        self.y = get_canvas_height() / 2
        self.velocity = BackSpeed[depth]


    def render(self):
        self.image.draw(self.x, self.y, get_canvas_width(),get_canvas_height())

    def update(self):
        self.x -= self.velocity

class BackGround:
    def __init__(self):
        self.images = [[] for _ in range(5)]
        for layer in range(5):
            for i in range(1,4):
                self.images[layer].append(BackImage(layer,i))



    def update(self):
        for layer in self.images:
            for i in layer:
                i.update()

    def render(self):
        for layer in self.images:
            for i in layer:
                i.render()


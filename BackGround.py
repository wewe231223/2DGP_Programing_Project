import math

from pico2d import load_image, draw_rectangle , get_canvas_width , get_canvas_height
from random import randint
import random

def CreateVelocity():
    result = random.sample(range(1, 100), 5)
    result.sort()
    floatresult = []
    for i in result:
        floatresult.append( float(i) / 100.0 )

    print(floatresult)
    return floatresult


BackSpeed = CreateVelocity()

class BackImage:
    def __init__(self,depth,position = 1):
        self.image = load_image("./Resources/BackGround_1/"+"%d"%(5-depth)+".png")
        self.x = (get_canvas_width() / 2) * (position * 2 - 1)
        self.y = get_canvas_height() / 2
        self.velocity = BackSpeed[depth]
        self.prevImage = None
        self.bb_y = None

        if depth == 4:
            self.bb_y = 30



    def render(self):
        self.image.draw(self.x, self.y, get_canvas_width(),get_canvas_height())
      #  draw_rectangle(*self.get_bb())

    def update(self):
        if self.x < -get_canvas_width() :
            self.x = self.prevImage.x + get_canvas_width() / 2
        else:
            self.x -= self.velocity

    def get_bb(self):
        if self.bb_y:
            return self.x - get_canvas_width() / 2 , self.bb_y - 30, self.x + get_canvas_width() / 2 , self.bb_y + 30
        else: return None

class BackGround:
    def __init__(self):
        self.images = [[] for _ in range(5)]

        index = 0
        for layer in self.images:

            layer.append(BackImage(index,1))
            layer.append(BackImage(index, 2))
            layer.append(BackImage(index, 3))

            layer[0].prevImage = layer[-1]
            layer[1].prevImage = layer[0]
            layer[2].prevImage = layer[1]

            index += 1




    def update(self):
        for layer in self.images:
            for i in layer:
                i.update()

    def render(self):
        for layer in self.images:
            for i in layer:
                i.render()
                if i.bb_y:
                    draw_rectangle(*i.get_bb())



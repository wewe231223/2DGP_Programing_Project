import math

from pico2d import load_image, draw_rectangle , get_canvas_width , get_canvas_height
from random import randint
import random




def CreateVelocity():

    result = random.sample(range(1, 100), 5)

    result.sort()

    floatresult = []
    for i in result:
        floatresult.append( float(i) / 1000.0 )

    print(floatresult)

    return floatresult


class BackGroundImage:
    def __init__(self,path,x = None):
        self.image = load_image(path)
        if x:
            self.x = x
        else:
            self.x = get_canvas_width() / 2
        self.y = get_canvas_height() / 2
        self.velocity = 0

    def update(self):
        self.x -= self.velocity

    def render(self):
        self.image.draw(self.x,self.y,get_canvas_width(),get_canvas_height())

global v
v = CreateVelocity()
class BackGround:
    def __init__(self, x = None):
        self.image1 = BackGroundImage("Resources/BackGround_1/1.png",x)
        self.image2 = BackGroundImage("Resources/BackGround_1/2.png",x)
        self.image3 = BackGroundImage("Resources/BackGround_1/3.png",x)
        self.image4 = BackGroundImage("Resources/BackGround_1/4.png",x)
        self.image5 = BackGroundImage("Resources/BackGround_1/5.png",x)


        self.image1.velocity = v[0]
        self.image2.velocity = v[1]
        self.image3.velocity = v[2]
        self.image4.velocity = v[3]
        self.image5.velocity = v[4]


    def update(self):
        self.image1.update()
        self.image2.update()
        self.image3.update()
        self.image4.update()
        self.image5.update()


    def render(self):
        self.image5.render()
        self.image4.render()
        self.image3.render()
        self.image2.render()
        self.image1.render()


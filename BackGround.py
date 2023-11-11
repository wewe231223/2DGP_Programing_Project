import math

from pico2d import load_image, draw_rectangle , get_canvas_width , get_canvas_height
from random import randint
import random

from input_event_functions import *

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
        self.prevImage = None
        self.bb_y = None

        if depth == 4:
            self.bb_y = 30



    def render(self):
        self.image.draw(self.x, self.y, get_canvas_width(),get_canvas_height())
      #  draw_rectangle(*self.get_bb())

    def update(self):
        if self.x < -get_canvas_width() / 2  :
            self.x = self.prevImage.x + get_canvas_width() - 5
        else:
            self.x -= self.velocity

    def get_bb(self):
        if self.bb_y:
            return self.x - get_canvas_width() / 2 , self.bb_y - 30, self.x + get_canvas_width() / 2 , self.bb_y + 30
        else: return None

class Idle:

    @staticmethod
    def enter(background,event):
        pass

    @staticmethod
    def exit(background,event):
        pass

    @staticmethod
    def do(background):
        pass


    @staticmethod
    def draw(background):
        for layer in background.images:
            for backgroundimage in layer:
                backgroundimage.render()
                if backgroundimage.bb_y:
                    draw_rectangle(*backgroundimage.get_bb())


class Scroll:

    @staticmethod
    def enter(background, event):
        pass

    @staticmethod
    def exit(background, event):
        pass

    @staticmethod
    def do(background):
        for layer in background.images:
            for backgroundimage in layer:
                backgroundimage.update()


    @staticmethod
    def draw(background):
        for layer in background.images:
            for backgroundimage in layer:
                backgroundimage.render()
                if backgroundimage.bb_y:
                    draw_rectangle(*backgroundimage.get_bb())


class BackGround_Statemachine:
    def __init__(self,back):
        self.Back = back
        self.cur_state = Idle
        self.transitions = {
            Idle: {right_down : Scroll},
            Scroll: {right_up : Idle}
        }

    def start(self):
        self.cur_state.enter(self.Back,("None",0))

    def update(self):
        self.cur_state.do(self.Back)

    def handle_event(self,e):
        for check_event, next_state in self.transitions[self.cur_state].items():
            if check_event(e):
                self.cur_state.exit(self.Back,e)
                self.cur_state = next_state
                self.cur_state.enter(self.Back,e)
                return True
        return False


    def draw(self):
        self.cur_state.draw(self.Back)




class BackGround:
    def __init__(self):
        self.images = [[] for _ in range(5)]
        self.statemachine = BackGround_Statemachine(self)

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
        self.statemachine.update()

    def render(self):
        self.statemachine.draw()

    def handle_event(self,event):
        self.statemachine.handle_event(("INPUT",event))



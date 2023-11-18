import math

from pico2d import load_image, draw_rectangle , get_canvas_width , get_canvas_height
from random import randint
import random

import Timer
from input_event_functions import *

def CreateVelocity():
    result = random.sample(range(1, 100), 5)
    result.sort()
    floatresult = []
    for i in result:
        floatresult.append( float(i) / 1000.0 )

    print(floatresult)
    return floatresult


BackSpeed = CreateVelocity()



class Idle:

    @staticmethod
    def enter(background,event):
        pass


    @staticmethod
    def exit(background,event):
        background.acceleration = 1


    @staticmethod
    def do(background):
        background.velocity += background.acceleration * Timer.delta_time
        if background.velocity <= 0.0 : background.velocity = 0.0

        if background.x < -get_canvas_width() / 2:
            background.x = background.prevImage.x + get_canvas_width() - background.velocity
        else:
            background.x -= background.velocity
        pass


    @staticmethod
    def draw(background):
        background.image.draw(background.x, background.y, get_canvas_width(),get_canvas_height())
        if background.bb_y:
            draw_rectangle(*background.get_bb())


class Scroll:

    @staticmethod
    def enter(background, event):
        pass

    @staticmethod
    def exit(background, event):
        background.acceleration = -1

    @staticmethod
    def do(background):

        background.velocity += background.acceleration * Timer.delta_time
        clamp(0.0,background.velocity,background.velocity)

        if background.x < -get_canvas_width() / 2:
            background.x = background.prevImage.x + get_canvas_width() - background.velocity
        else:
            background.x -= background.velocity



    @staticmethod
    def draw(background):
        background.image.draw(background.x, background.y, get_canvas_width(), get_canvas_height())
        if background.bb_y:
            draw_rectangle(*background.get_bb())


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
    def __init__(self,depth,position):
        self.image = load_image("./Resources/BackGround_1/" + "%d" % (5 - depth) + ".png")
        self.x = (get_canvas_width() / 2) * (position * 2 - 1)
        self.y = get_canvas_height() / 2
        self.max_velocity = BackSpeed[depth]
        self.velocity = 0.0
        self.acceleration = 0.0
        self.prevImage = None
        self.bb_y = None
        self.statemachine = BackGround_Statemachine(self)

        if depth == 4:
            self.bb_y = 20


    def render(self):
        self.statemachine.draw()


    def update(self):
        self.statemachine.update()

    def get_bb(self):
        if self.bb_y:
            return self.x - get_canvas_width() / 2, 0, self.x + get_canvas_width() / 2, 50
        else: return None


    def handle_event(self,event):
        self.statemachine.handle_event(("INPUT",event))

    def handle_collision(self,group,other):
        pass

import math
from sys import float_info

from pico2d import load_image, draw_rectangle , get_canvas_width , get_canvas_height
import random

import Timer
from input_event_functions import *


MAX_VELOCITY = 13.0
Scroll_speed = [0.1,0.2,0.4,0.8,1.6]
Scroll_max_speed = [3,6,12,18,25]


DeScroll_speed = Scroll_speed.copy()
DeScroll_speed.reverse()


class Idle:

    @staticmethod
    def enter(background,event):
        pass


    @staticmethod
    def exit(background,event):
        background.acceleration = Scroll_speed[background.depth]


    @staticmethod
    def do(background):
        background.velocity *= 0.999
        if background.velocity < float_info.epsilon:
            background.velocity = 0.0

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
        background.velocity += Scroll_speed[background.depth]
        pass

    @staticmethod
    def exit(background, event):
        background.acceleration = -5


    @staticmethod
    def do(background):
        if  background.velocity < Scroll_max_speed[background.depth]:
            background.velocity *= 1.001

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
        self.max_velocity = Scroll_speed[depth]
        print(self.max_velocity)
        self.velocity = 0.0
        self.acceleration = 0.0
        self.depth = depth
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

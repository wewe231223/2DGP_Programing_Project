
from pico2d import *


def right_down(e):

    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_RIGHT

def right_not_donw(e):
    return not right_down(e)

def right_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_RIGHT


def space_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_SPACE


def space_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_SPACE


def end(e):
    return e[0] == 'ANIMATION_END'

def landing(e):
    return e[0] == "LANDED"

def jumped(e):
    return e[0] == "JUMPED"

def idle(e):
    return True

def dead(e):
    return e[0] == "DEAD"



def over(e):
    return e[0] == "OVER"
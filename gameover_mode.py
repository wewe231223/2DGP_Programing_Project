import game_framework
from pico2d import *
import game_world


def handle_events():
    events = get_events()


    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()

        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()

        else:
            game_world.handle_event(event)




def init():

    pass



def finish():
    pass


def update():
    pass



def draw():
    pass

def pause():
    pass


def resume():
    pass

import game_framework
from pico2d import *
import game_world
import server
from ui import UI

import play_mode

def handle_events():
    events = get_events()


    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            play_mode.finish()
            game_framework.change_mode(play_mode)
        else:
            game_world.handle_event(event)




def init():
    server.ui_object.is_over = True
    pass



def finish():
    pass


def update():
    game_world.update()


def draw():
    clear_canvas()


    game_world.render()
    update_canvas()
def pause():
    pass


def resume():
    pass

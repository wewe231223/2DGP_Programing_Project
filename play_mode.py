from pico2d import *

import Game
import game_world

from Character import Character


def handle_events():
    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            Game.quit()

        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            Game.quit()

        else:
            main_character.handle_event(event)



def init():
    global main_character

    main_character = Character()
    game_world.add_object(main_character,0)

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

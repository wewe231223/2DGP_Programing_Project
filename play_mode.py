from pico2d import *

import Game

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



world = []
def init():
    global main_character

    main_character = Character()
    world.append(main_character)


def finish():
    pass


def update():
    for o in world:
        o.update()


def draw():
    clear_canvas()
    for o in world:
        o.render()
    update_canvas()

def pause():
    pass

def resume():
    pass

import pico2d
from pico2d import *

open_canvas()

character = load_image("Resources/character_animations.png")



def handleevent(events):
    for event in events:
        if event.type == SDL_QUIT:
            exit(0)
        if event.type ==SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            exit(0)

Eventlist = []

while True:
    clear_canvas()

    character.clip_draw(0,150,150,150,400,400);

    Eventlist = get_events()

    handleevent(Eventlist)

    update_canvas()

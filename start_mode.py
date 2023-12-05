import explain_mode
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
            game_framework.change_mode(explain_mode)
        else:
            game_world.handle_event(event)

start_image = None


def init():
    global start_image,font,titlefont

    start_image = load_image("./Resources/Start.png")


    font = load_font('./Resources/Pixel.ttf', 50)
    titlefont = load_font('./Resources/Pixel.ttf', 100)


def finish():
    pass


def update():
    game_world.update()


def draw():
    clear_canvas()

    start_image.draw(1920 / 2, 1080 / 2, 1920, 1080)
    titlefont.draw(1920/2  - 580,1080 - 200 , "Snowman Ski")
    font.draw(1920/2 - 300, 1080 / 2- 500, "Press Space")

    update_canvas()

    pass
def pause():
    pass


def resume():
    pass

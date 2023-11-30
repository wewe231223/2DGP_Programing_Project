from pico2d import *

import game_framework
import game_world

from Character import Character
from BackGround import BackGround
import server
from Obastcle import Obstacle
from ui import UI


import util


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

    global background_1_1,background_1_2,background_1_3, background_2_1,background_2_2,background_2_3, background_3_1,background_3_2,background_3_3, background_4_1,background_4_2,background_4_3, background_5_1,background_5_2,background_5_3


    game_world.add_object(Obstacle(),5)
    game_world.add_object(UI(),5)

    server.Maincharacter = Character()
    game_world.add_object(server.Maincharacter, 5)

    background_1_1 = BackGround(0,1)
    background_1_2 = BackGround(0, 2)
    background_1_3 = BackGround(0, 3)

    background_1_1.prevImage = background_1_3
    background_1_2.prevImage = background_1_1
    background_1_3.prevImage = background_1_2

    background_2_1 = BackGround(1, 1)
    background_2_2 = BackGround(1, 2)
    background_2_3 = BackGround(1, 3)

    background_2_1.prevImage = background_2_3
    background_2_2.prevImage = background_2_1
    background_2_3.prevImage = background_2_2

    background_3_1 = BackGround(2, 1)
    background_3_2 = BackGround(2, 2)
    background_3_3 = BackGround(2, 3)


    background_3_1.prevImage = background_3_3
    background_3_2.prevImage = background_3_1
    background_3_3.prevImage = background_3_2

    background_4_1 = BackGround(3, 1)
    background_4_2 = BackGround(3, 2)
    background_4_3 = BackGround(3, 3)


    background_4_1.prevImage = background_4_3
    background_4_2.prevImage = background_4_1
    background_4_3.prevImage = background_4_2

    background_5_1 = BackGround(4, 1)
    background_5_2 = BackGround(4, 2)
    background_5_3 = BackGround(4, 3)


    # sample ground to sample ground velocity
    server.GroundSample = background_5_1



    background_5_1.prevImage = background_5_3
    background_5_2.prevImage = background_5_1
    background_5_3.prevImage = background_5_2



    game_world.add_objects([background_1_1, background_1_2, background_1_3], 0)
    game_world.add_objects([background_2_1, background_2_2, background_2_3], 1)
    game_world.add_objects([background_3_1, background_3_2, background_3_3], 2)
    game_world.add_objects([background_4_1, background_4_2, background_4_3], 3)
    game_world.add_objects([background_5_1, background_5_2, background_5_3], 4)


    game_world.add_collision_pair("Ground_Character",server.Maincharacter,None)

    game_world.add_collision_pair("Ground_Character", None,         background_5_1)
    game_world.add_collision_pair("Ground_Character", None,         background_5_2)
    game_world.add_collision_pair("Ground_Character", None,         background_5_3)







def finish():
    pass


def update():
    if util.random_percent(0.001):
        game_world.add_object(Obstacle(),5)

    game_world.update()
    game_world.handle_collisions()




def draw():
    clear_canvas()
    game_world.render()
    update_canvas()


def pause():
    pass


def resume():
    pass

import pico2d
import random

import game_world
import server


class Obstacle:
    images = []


    def __init__(self):
        if not Obstacle.images:
            for i in range(0, 5):
                temp = pico2d.load_image("./Resources/snowy_rock" + "%d" % (i) + ".png")
                Obstacle.images.append(temp)
        self.type = random.randint(0, 4)
        self.image = Obstacle.images[self.type]
        self.x = 1920
        self.statemachine = None
        self.y = 150


    def render(self):
        self.image.draw(self.x,self.y,200,200)
        pico2d.draw_rectangle(*self.get_bb())

    def update(self):
        self.x -= server.GroundSample.velocity
        if self.x < -10:
            game_world.remove_object(self)
            game_world.remove_collision_object(self)



    def handle_event(self,event):
        pass

    def get_bb(self):
        return self.x - 100, self.y - 100, self.x + 100, self.y + 100

    def handle_collision(self,group,other):
        pass






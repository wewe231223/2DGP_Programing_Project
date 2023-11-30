import pico2d
import random

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
        self.y = 100



    def render(self):
        self.image.draw(self.x,self.y)

    def update(self):
        self.x -= server.GroundSample.velocity

    def handle_event(self,event):
        pass

    def handle_collision(self,group,other):
        pass








import pico2d



class Tilemap:
    image = None



    def load_image(self):
        if Tilemap.image == None:
            Tilemap.image = pico2d.load_image("./Resources/Tiles.png")
    def __init__(self,raw,column):
        self.raw = raw
        self.column = column
        self.load_image()


    def render(self):
        Tilemap.image.clip_draw(self.raw * 144, self.column * 144,144,144,500,500)


    def update(self):
        pass

    def handle_event(self,event):
        pass


import pico2d

TILE_INTERVAL = 94



class Tilemap:
    image = None



    def load_image(self):
        if Tilemap.image == None:
            Tilemap.image = pico2d.load_image("./Resources/Tiles.png")
    def __init__(self,raw,column,x,y):
        self.raw = raw
        self.column = column
        self.load_image()
        self.x, self.y  = x, y



    def render(self):
        Tilemap.image.clip_draw(self.raw * 144, self.column * 144,144,144,self.x,self.y)
        pico2d.draw_rectangle(*self.get_bb())

    def update(self):
        pass

    def handle_event(self,event):
        pass

    def get_bb(self):
        return self.x - 48, self.y- 48, self.x + 48, self.y + 48



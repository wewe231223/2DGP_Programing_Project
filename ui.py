
from pico2d import load_image
import server


class UI:
    image_loaded = False
    heart_image = None

    def __init__(self):
        if not UI.image_loaded:
            UI.heart_image = load_image('./Resources/heart pixel art 64x64.png')

        self.heartimg = UI.heart_image



    def render(self):
        self.render_heart()

    def render_heart(self):
        character_heart = server.Maincharacter.heart

        layoutx = 60
        layouty = 60

        for hp in range(character_heart):
            self.heartimg.draw(1920 - layoutx,1080 - layouty)
            layoutx += 80

    def update(self):
        pass

    def handle_event(self,event):
        pass

    def handle_collision(self,group,other):
        pass


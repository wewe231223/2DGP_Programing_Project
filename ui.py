
from pico2d import load_image, load_font
import server

KMPH = 0.0

class UI:
    image_loaded = False
    heart_image = None

    def __init__(self):
        if not UI.image_loaded:
            UI.heart_image = load_image('./Resources/heart pixel art 64x64.png')
            UI.Font = load_font('./Resources/Pixel.ttf',50)
            UI.image_loaded = True
        self.heartimg = UI.heart_image
        self.font = UI.Font
        self.timeforoneblock = 180.0
        self.statemachine = None


        self.is_over = False



    def render(self):
        self.render_heart()
        self.render_velocity()
        self.render_score()
        if self.is_over:
            self.render_over()

    def render_heart(self):
        character_heart = server.Maincharacter.heart

        layoutx = 60
        layouty = 60
        for hp in range(character_heart):
            self.heartimg.draw(1920 - layoutx,1080 - layouty)
            layoutx += 80


    def render_score(self):
        score = server.Score

        self.font.draw(50,900,f'Score : { int(score)}')

    def render_velocity(self):

        self.font.draw(0,1050,  f'{round(KMPH,4) : 1f}' + " KM/H")

    def render_over(self):
        self.font.draw(1920 / 2 - 300, 1080/  2, "Play Again?")

        self.font.draw(1920 / 2 - 300, 1080 / 2  - 100, "Press Space ")



    def update(self):
        pass

    def handle_event(self,event):
        pass

    def handle_collision(self,group,other):
        pass


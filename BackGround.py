from pico2d import load_image



class BackGround:
    def __init__(self):
        self.image = load_image("Resources/BackGround_1/0.png")


    def render(self):
        self.image.draw(960, 540, 1920, 1080)
        pass
    def update(self):

        pass

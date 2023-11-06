from pico2d import *
from Character import *
from BackGround import BackGround
global running



class Game:
    def __init__(self):
        self.world = [[],[]]

        self.reset()


    def update(self):
        global running
        events = get_events()

        for event in events:
            if event.type == SDL_QUIT:
                exit(0)
            if event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                exit(0)


        for layer in self.world:
           for object in layer:
               object.update()


    def reset(self):
        open_canvas(1920, 1080)

        character = Character()
        backGround = BackGround()
        self.world[0].append(backGround)
        self.world[1].append(character)

        pass


    def render(self):
        for layer in self.world:
           for object in layer:
               object.render()



    def run(self):



        while True:
            clear_canvas()

            self.update()
            self.render()

            update_canvas()
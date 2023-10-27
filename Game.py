from pico2d import *
from Character import *
global running



class Game:
    def __init__(self):
        self.world = []

        self.reset()


    def update(self):
        global running
        events = get_events()

        for event in events:
            if event.type == SDL_QUIT:
                exit(0)
            if event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                exit(0)


        for o in self.world:
            o.update()


    def reset(self):
        open_canvas()

        character = Character()
        self.world.append(character)
        pass


    def render(self):
        for o in self.world:
            o.render()



    def run(self):



        while True:
            clear_canvas()

            self.update()
            self.render()

            update_canvas()
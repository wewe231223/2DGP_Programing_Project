from pico2d import *

import Timer

CHARACTER_TIME_PER_ACTION = 0.7
ACTION_PER_TIME =1.0 / CHARACTER_TIME_PER_ACTION



Behavior_Frame = {
 0: 4,
 1: 1,
 2: 8,
 3: 3,
 4: 7,
 5: 3,
 6: 5
}

def right_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_RIGHT


def right_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_RIGHT


class Idle:
    @staticmethod
    def enter(ch,e):
        ch.action = 3
        pass

    @staticmethod
    def exit(ch,e):
        pass
    @staticmethod
    def do(ch):
        ch.frame = (ch.frame + Behavior_Frame[ch.action] * ACTION_PER_TIME * Timer.delta_time) % Behavior_Frame[ch.action]

    @staticmethod
    def draw(ch):
        ch.image.clip_draw(int(ch.frame) * ch.width, ch.width * ch.action, ch.width, ch.width, ch.x, ch.y,300,300)


class Forward:
    @staticmethod
    def enter(ch, e):
        ch.action = 6b  
        pass

    @staticmethod
    def exit(ch, e):
        pass

    @staticmethod
    def do(ch):
        ch.x += 0.001
        ch.frame = (ch.frame+ Behavior_Frame[ch.action] * ACTION_PER_TIME * Timer.delta_time) % Behavior_Frame[ch.action]

    @staticmethod
    def draw(ch):
        ch.image.clip_draw(int(ch.frame) * ch.width, ch.width * ch.action, ch.width, ch.width, ch.x, ch.y, 300, 300)


class Character_StateMachine:

    def __init__(self,character):
        self.character = character
        self.cur_state = Idle
        self.transitions = {
            Idle : {right_down : Forward},
            Forward : {right_up : Idle}
        }


    def start(self):
        self.cur_state.enter(self.character,('NONE', 0))

    def update(self):
        self.cur_state.do(self.character)

    def handle_event(self,e):
        for check_event, next_state in self.transitions[self.cur_state].items():
            if check_event(e):
                self.cur_state.exit(self.character,e)
                self.cur_state = next_state
                self.cur_state.enter(self.character,e)
                return True
        return False

    def draw(self):
        self.cur_state.draw(self.character)


class Character:
    def __init__(self):
        self.image = load_image("Resources/character_animations.png")
        self.action = 4
        self.width = 150
        self.height = 150
        self.x = 300
        self.y = 300
        self.action = 6
        self.frame = 0
        self.statemachine = Character_StateMachine(self)
        self.statemachine.start()

    def render(self):
        self.statemachine.draw()

    def update(self):
        self.statemachine.update()

    def handle_event(self,event):
        self.statemachine.handle_event(("INPUT",event))
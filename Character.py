from pico2d import *

import Timer

from input_event_functions import *

CHARACTER_TIME_PER_ACTION = 0.7
ACTION_PER_TIME =1.0 / CHARACTER_TIME_PER_ACTION





Behavior_Frame = {
 "DEAD": 4,
 "LINK_DEAD": 1,
 "COLLIDE": 8,
 "SLIDE_DOWN": 3,
 "JUMP": 7,
 "WEAVE": 3,
 "BOOST": 5
}

Behavior_Action= {
    "DEAD": 0,
    "LINK_DEAD": 1,
    "COLLIDE": 2,
    "SLIDE_DOWN": 3,
    "JUMP": 4,
    "WEAVE": 5,
    "BOOST": 6
}



class Idle:
    @staticmethod
    def enter(ch,e):
        ch.action = "SLIDE_DOWN"
        ch.bb_y = 35
        pass

    @staticmethod
    def exit(ch,e):
        pass
    @staticmethod
    def do(ch):
        ch.frame = (ch.frame + Behavior_Frame[ch.action] * ACTION_PER_TIME * Timer.delta_time) % Behavior_Frame[ch.action]

    @staticmethod
    def draw(ch):
        ch.image.clip_draw(int(ch.frame) * ch.width, ch.width * Behavior_Action[ch.action], ch.width, ch.width, ch.x, ch.y,300,300)


class Forward:
    @staticmethod
    def enter(ch, e):
        ch.action = "BOOST"
        ch.bb_y = 40
        pass

    @staticmethod
    def exit(ch, e):
        pass

    @staticmethod
    def do(ch):
        ch.frame = (ch.frame+ Behavior_Frame[ch.action] * ACTION_PER_TIME * Timer.delta_time) % Behavior_Frame[ch.action]

    @staticmethod
    def draw(ch):
        ch.image.clip_draw(int(ch.frame) * ch.width, ch.width * Behavior_Action[ch.action], ch.width, ch.width, ch.x, ch.y, 300, 300)


class Jump:
    @staticmethod
    def enter(ch, e):
        ch.action = "JUMP"
        ch.y = 200
        pass

    @staticmethod
    def exit(ch, e):
        pass

    @staticmethod
    def do(ch):
        if int(ch.frame) == Behavior_Frame[ch.action] - 1:
            ch.statemachine.handle_event(("ANIMATION_END",0))
        else :
            ch.frame = (ch.frame + Behavior_Frame[ch.action] * ACTION_PER_TIME * 0.5 * Timer.delta_time) % Behavior_Frame[ch.action]

    @staticmethod
    def draw(ch):
        ch.image.clip_draw( int(ch.frame) * ch.width, ch.width * Behavior_Action[ch.action], ch.width, ch.width, ch.x, ch.y, 300, 300 )

class ReadyJump:

    @staticmethod
    def enter(character,event):
        pass

    @staticmethod
    def exit(character,event):
        pass

    @staticmethod
    def do(character):
        pass

    @staticmethod
    def draw(character):
        pass

    



class Character_StateMachine:

    def __init__(self,character):
        self.character = character
        self.cur_state = Idle
        self.transitions = {
            Idle: {right_down : Forward, space_down : Jump},
            Forward: {right_up : Idle, space_down : Jump},
            Jump: {end: Idle}
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
        self.action = "SLIDE_DOWN"
        self.width = 150
        self.height = 150
        self.x = 300
        self.y = 300
        self.action = 6
        self.frame = 0
        self.bb_y = 40
        self.statemachine = Character_StateMachine(self)
        self.statemachine.start()


        self.delta_y = 0


    def render(self):
        self.statemachine.draw()
        draw_rectangle(*self.get_bb())


 #       self.test.clip_draw(0,144 * self.testx,144,144,100,100)

    def update(self):
        self.statemachine.update()
        self.delta_y = -1
        self.y += self.delta_y



    def handle_event(self,event):
        self.statemachine.handle_event(("INPUT",event))

    def handle_collision(self,group,other):
        self.y -= self.delta_y

        pass

    def get_bb(self):
        return self.x - 40, self.y -self.bb_y, self.x + 40, self.y + self.bb_y
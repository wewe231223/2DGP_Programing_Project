import pico2d
from pico2d import *

import Timer
import game_framework
import game_world
import server
import gameover_mode

from input_event_functions import *

CHARACTER_TIME_PER_ACTION = 0.7
ACTION_PER_TIME =1.0 / CHARACTER_TIME_PER_ACTION

# 150 pixel = 0.75m


CHARACTER_STOPWATCH_ID = 1
CHARACTER_INVINCIBLE_TIME = 2.0




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
        ch.y += 1
        ch.bb_y = 40
        ch.slidesound = load_wav("./Resources/slide_snow.wav")
        ch.slidesound.repeat_play()
        pass

    @staticmethod
    def exit(ch, e):
        ch.slidesound = None
        pass

    @staticmethod
    def do(ch):
        ch.frame = (ch.frame+ Behavior_Frame[ch.action] * ACTION_PER_TIME * Timer.delta_time) % Behavior_Frame[ch.action]


    @staticmethod
    def draw(ch):
        ch.image.clip_draw(int(ch.frame) * ch.width, ch.width * Behavior_Action[ch.action], ch.width, ch.width, ch.x, ch.y, 300, 300)


class Jump:
    @staticmethod
    def enter(character, e):
        character.frame = 1
        character.bb_y = 35
        character.jumpsound.play(1)


    @staticmethod
    def exit(ch, e):
        ch.frame = 0


    @staticmethod
    def do(character):
        if int(character.frame) < 6:
            character.frame = (character.frame + Behavior_Frame[character.action] * ACTION_PER_TIME * Timer.delta_time) % Behavior_Frame[character.action]

        character.Y_Acceleration -= 10 * Timer.delta_time
        character.y += character.Y_Acceleration


    @staticmethod
    def draw(ch):
        ch.image.clip_draw( int(ch.frame) * ch.width, ch.width * Behavior_Action[ch.action], ch.width, ch.width, ch.x, ch.y, 300, 300 )



class ReadyJump:

    @staticmethod
    def enter(character,event):
        character.frame = 0
        character.bb_y = 40
        character.action = "JUMP"
        Timer.Start_Watch(CHARACTER_STOPWATCH_ID)

        print("Charge")

    @staticmethod
    def exit(character,event):
        character.Y_Acceleration = clamp(0.0,Timer.Get_Elapsed(CHARACTER_STOPWATCH_ID) * 15,10.0)

        pass

    @staticmethod
    def do(character):
        print("Charging...")
        if int(character.frame) == 1:
            character.statemachine.handle_event(("ANIMATION_END",0))
        else :
            character.frame = (character.frame + Behavior_Frame[character.action] * ACTION_PER_TIME * Timer.delta_time) % Behavior_Frame[character.action]


    @staticmethod
    def draw(character):
        character.image.clip_draw( int(character.frame) * character.width, character.width * Behavior_Action[character.action], character.width, character.width, character.x, character.y, 300, 300 )

        pass

class land:

    @staticmethod
    def enter(character,event):
        pass
    @staticmethod
    def exit(character, event):
        pass

    @staticmethod
    def do(character):

        pass

    @staticmethod
    def draw(character):
        character.image.clip_draw( int(character.frame) * character.width, character.width * Behavior_Action[character.action], character.width, character.width, character.x, character.y, 300, 300 )

class Dead:

    @staticmethod
    def enter(character,event):
        character.action = "COLLIDE"
        character.bb_y = 50
        character.y += 20

    @staticmethod
    def exit(character, event):
        character.action = "DEAD"

        game_framework.push_mode(gameover_mode)

    @staticmethod
    def do(character):
        if int(character.frame) == Behavior_Frame[character.action] - 1:
            server.Maincharacter.statemachine.handle_event(("OVER",0))
            for background in server.BackGrounds:
                background.statemachine.handle_event(("OVER",0))

        else :
            character.frame = (character.frame + Behavior_Frame[character.action] * ACTION_PER_TIME * Timer.delta_time) % Behavior_Frame[character.action]


        character.Y_Acceleration -= 10 * Timer.delta_time
        character.y += character.Y_Acceleration

    @staticmethod
    def draw(character):
        character.image.clip_draw( int(character.frame) * character.width, character.width * Behavior_Action[character.action], character.width, character.width, character.x, character.y, 300, 300 )


class Over:

    @staticmethod
    def enter(character,event):
        character.opacity = 1.0
        character.diesound.play(1)
        pass

    @staticmethod
    def exit(character, event):
        pass

    @staticmethod
    def do(character):
        character.frame = (character.frame + Behavior_Frame[character.action] * ACTION_PER_TIME * Timer.delta_time) % Behavior_Frame[character.action]

    @staticmethod
    def draw(character):
        character.image.clip_draw(int(character.frame) * character.width, character.width * Behavior_Action[character.action], character.width, character.width, character.x, character.y, 300, 300 )





class Character_StateMachine:

    def __init__(self,character):
        self.character = character
        self.cur_state = Idle
        self.transitions = {
            Idle: {right_down : Forward, space_down : ReadyJump, dead : Dead},
            Forward: {right_up : Idle, space_down : ReadyJump,dead : Dead},
            ReadyJump: {space_up: Jump,dead : Dead},
            Jump: {landing: land,dead : Dead},
            land: {right_down : Forward, right_not_donw : Idle,dead : Dead},
            Dead:{over : Over},
            Over : {}
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
        self.character.image.opacify(self.character.opacity)
        self.cur_state.draw(self.character)




class Character:
    def __init__(self):
        self.image = load_image("Resources/character_animations.png")
        self.action = "SLIDE_DOWN"
        self.width = 150
        self.height = 150
        self.x = 300
        self.y = 100
        self.action = 6
        self.frame = 0
        self.bb_y = 0
        self.statemachine = Character_StateMachine(self)
        self.statemachine.start()
        self.Y_Acceleration = 0.0
        self.heart = 5
        self.delta_y = 0
        self.slidesound = None
        self.jumpsound = load_wav("./Resources/jump.wav")
        self.damagesound = load_wav("./Resources/damage.wav")
        self.diesound = load_wav("./Resources/die.wav")




        self.opacity = 1.0
        self.invincible_counter = 0.0



    def render(self):
        self.statemachine.draw()
        #draw_rectangle(*self.get_bb())


 #       self.test.clip_draw(0,144 * self.testx,144,144,100,100)

    def update(self):

        self.statemachine.update()




        if self.opacity == 0.5:
            self.invincible_counter += Timer.delta_time
        if self.invincible_counter > CHARACTER_INVINCIBLE_TIME:
            self.disinvincible()
        if self.heart == 0:
            self.statemachine.handle_event(("DEAD",0))


    def handle_event(self,event):
        self.statemachine.handle_event(("INPUT",event))

    def handle_collision(self,group,other):


        if(group == 'Ground_Character'):
            self.y -= self.delta_y
            self.Y_Acceleration = 0.0
            self.statemachine.handle_event(("LANDED",0))
        if(group == "Obstacle_Character" or group == "Eagle_Character"):
            if self.opacity == 1.0:
                self.damagesound.play(1)
                self.heart -= 1
                self.invincible()



    def get_bb(self):
        return self.x - 40, self.y -self.bb_y, self.x + 40, self.y + self.bb_y

    def invincible(self):
        self.opacity = 0.5

    def disinvincible(self):
        self.opacity = 1.0
        self.invincible_counter = 0.0

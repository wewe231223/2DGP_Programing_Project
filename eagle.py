from pico2d import load_image, draw_rectangle
import math

import Timer
import game_world
import server



CHARACTER_TIME_PER_ACTION = 0.7
ACTION_PER_TIME = 1.0 / CHARACTER_TIME_PER_ACTION

ImageSize = {
    0:38,
    1:41,
    2:40,
    3:43,
    4:40,
    5:43,
    6:43,
    7:42,
    8:41,
    9:40,
    10:41,
    11:43,
    12:42,
    13:41
}
def image_pivot(frame):
    s = 0
    f = 0
    for k, v in ImageSize.items():
        if f == frame : return s
        s += v
        f += 1

    return s


def distance(a,b):
    return math.sqrt((b[0] - a[0])**2 + (b[1] - a[1])**2 )


class Eagle:
    image = None

    def __init__(self):
        if Eagle.image == None:
            Eagle.image = load_image("./Resources/eagle.png")

        self.img = Eagle.image

        self.frame = 0
        self.speed = 0.1
        self.max_speed = 1
        self.x = 1920
        self.y = 1080
        self.angle = math.atan2(server.Maincharacter.x - self.x, server.Maincharacter.y - self.y)

        self.dx = math.cos(self.angle) * self.speed
        self.dy = math.sin(self.angle) * self.speed
        self.tracking = True


    def update(self):
        self.frame = (self.frame + 160 * ACTION_PER_TIME * Timer.delta_time) % 14
        self.frame = int(self.frame)
        tx = server.Maincharacter.x
        ty = server.Maincharacter.y
        sx = self.x
        sy = self.y
        if self.tracking:

            self.angle = math.atan2(ty - sy, tx - sx)
            self.dx = math.cos(self.angle) * self.speed
            self.dy = math.sin(self.angle) * self.speed




            # 플레이어의 기체 x,y ±60 내로 접근 시, 추적을 멈춘다.
        if (distance((tx,ty),(sx,sy))):
            self.dx = math.cos(self.angle) * self.max_speed
            self.dy = math.sin(self.angle) * self.max_speed
            self.tracking = False

        self.x += self.dx
        self.y += self.dy


        if self.max_speed > self.speed:
            self.speed += 0.3


        if self.y < -50:
            game_world.remove_object(self)

        pass

    def render(self):
        pivot = image_pivot(self.frame)
        self.img.clip_draw(pivot,0,ImageSize[self.frame],50,self.x,self.y,200,200)
  #      draw_rectangle(*self.get_bb())


    def handle_event(self,event):
        pass

    def get_bb(self):
        return (self.x - 90, self.y - 30, self.x + 90, self.y + 30)


    def handle_collision(self,group,other):
        if group == "Eagle_Character":
            game_world.remove_collision_object(self)
            game_world.remove_object(self)
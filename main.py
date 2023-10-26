from pico2d import *

open_canvas()

character = load_image("Resources/Sprite.png")

while True:
    clear_canvas()

    character.draw(10, 10)

    update_canvas()

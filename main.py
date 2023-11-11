from pico2d import open_canvas, close_canvas

import Game
import play_mode as start_mode

open_canvas(1920,1080)

Game.run(start_mode)
close_canvas()
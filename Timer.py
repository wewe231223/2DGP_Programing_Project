import time



global prev_time, delta_time

def init():
    global prev_time, delta_time

    prev_time = time.time()
    delta_time = 0.0

def update():
    global prev_time, delta_time

    delta_time = time.time() - prev_time
    prev_time += delta_time



import time


Watch = []





global prev_time, delta_time

def init():
    global prev_time, delta_time

    prev_time = time.time()
    delta_time = 0.0

def update():
    global prev_time, delta_time

    delta_time = time.time() - prev_time
    prev_time += delta_time




def Start_Watch(id):

    # 아직 등록되지 않은 경우
    if(len(Watch) < id):
        Watch.append(time.time())
    else:
    # 등록되어 있는 경우
        Watch[id-1] = time.time()


def Get_Elapsed(id):
    return time.time() - Watch[id-1     ]



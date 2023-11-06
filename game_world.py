objects = [[] for _ in range(4)]




def add_object(o,depth = 0):
    objects[depth].append(o)





def update():
    for layer in objects:
        for o in layer:
            o.update()


def render():
    for layer in objects:
        for o in layer:
            o.render()




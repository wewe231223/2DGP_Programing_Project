objects = [[] for _ in range(6)]
collision_pairs = {}
import server


def add_object(object,depth = 0):
    objects[depth].append(object)


def add_objects(objectlist, depth = 0):
    objects[depth] += objectlist


def update():
    for layer in objects:
        for o in layer:
            if o is not None:
                o.update()


def render():
    for layer in objects:
        for o in layer:
            if o is not None:
                o.render()


def collide(a,b):
    left_a,bottom_a,right_a,top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True

def add_collision_pair(groupName,a,b):
    if groupName not in collision_pairs:
        collision_pairs[groupName] = [[],[]]

    if a:
        collision_pairs[groupName][0].append(a)
    if b:
        collision_pairs[groupName][1].append(b)


def handle_collisions():
    for group, pairs in collision_pairs.items():
        for a in pairs[0]:
            for b in pairs[1]:
                if collide(a, b):
                    a.handle_collision(group, a)
                    b.handle_collision(group, b)



def handle_event(event):
    for layer in objects:
        for object in layer:
            if object is not None :
                object.handle_event(event)
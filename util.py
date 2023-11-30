
import random

def random_percent(percentage):
    sample = random.random()


    if sample < percentage:
        return True
    else:
        return False

import random

def randomPair(a, b):
    if (b < a):
        a, b = b, a
    x_y_list = [0,0]
    for i in range(2):
        x_y_list[i] = random.randint(a, b)
    return x_y_list[0], x_y_list[1]

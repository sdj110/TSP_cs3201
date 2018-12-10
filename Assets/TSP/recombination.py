
from collections import deque
from numpy import random
from profiler import profile

def order_crossover(p1, p2):
    individual_size = len(p1)
    # generate 2 random ints from uniform distribution
    points = random.randint(1, individual_size - 1, 2) 
    if points[0] > points[1]:
        points[0], points[1] = points[1], points[0]

    off1 = [x for x in p2[points[0]:points[1]]]
    off2 = [x for x in p1[points[0]:points[1]]]

    for i in range(individual_size - 1, -1, -1):
        j = (i + points[1]) % individual_size
        if j >= points[0] and j < points[1]:
            continue
        off1.append(p2[j])
        off2.append(p1[j])
    return (off1, off2)

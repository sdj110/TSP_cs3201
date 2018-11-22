
from numpy import random

def order_crossover(parent0, parent1):
    """
        Takes two parent individuals and creates a single offspring
        using order crossover.
        args:
            parent0 : list
            parent1 : list
        return:
            List of Cities
    """
    individual_size = len(parent0)
    offspring = [None] * individual_size
    ## Generate random points
    points = random.randint(1, individual_size - 1, 2)
    while points[0] == points[1]:
        points = random.randint(1, individual_size - 1, 2)
    if (points[0] > points[1]):
            points[0], points[1] = points[1], points[0]
    ## Perform crossover to generate offspring
    for i in range(points[0], points[1] + 1):
        offspring[i] = parent0[i]
    i = points[1] + 1
    j = i
    while offspring[i] == None:
        while parent1[j] in offspring:
            j = (j + 1) % individual_size
        offspring[i] = parent1[j]
        i = (i + 1) % individual_size
    return offspring

    




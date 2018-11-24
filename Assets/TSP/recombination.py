
from collections import deque
from numpy import random
from profiler import profile

def order_crossover(parent1, parent2):
    """
        Performs order crossover to create two offspring from parent1 and parent2.
        args:
            parent0 : list
            parent1 : list
        return:
            tuple of two lists
    """
    individual_size = len(parent1)
    c1 = deque()
    c2 = deque()

    # generate 2 random ints from uniform distribution
    points = random.randint(1, individual_size - 1, 2) 
    if points[0] > points[1]:
        points[0], points[1] = points[1], points[0]

    # elements from interval [point[0], point[1]] from each parent are copied for ease of use
    # SJ: Might be a way to move this into main loop and remove some calculations
    region1 = [x for x in parent1[points[0] : points[1] + 1]]
    region2 = [x for x in parent2[points[0] : points[1] + 1]]

    # loop through parents and insert None in offspring at locations of values found in
    # other parent's [points[0], points[1]] index region. 
    for i in range(individual_size):
        if parent1[i] in region2:
            c1.appendleft(None)
        else:
            c1.append(parent1[i])

        if parent2[i] in region1:
            c2.appendleft(None)
        else:
            c2.append(parent2[i])
    # Use rotate to shift elements in children until all None values are located inside
    # childs [points[0], points[1]] index region.
    c1.rotate(points[0])
    c2.rotate(points[0])

    # Finally we relpace each child's [points[0], points[1]] index region with the 
    # opposite child's [points[0], points[1]] index.
    j = 0
    for i in range(points[0], points[1]+1):
        c1[i] = region2[j]
        c2[i] = region1[j]
        j += 1

    # Since children are deque object we use comprehension to
    # return lists
    # SJ: This is necessary because of how main is set up.
    # if this is expensive it might make more sense to use deques instead of lists since
    # this will be called many times.
    return ([x for x in c1], [x for x in c2])


def order_crossover_OLD(parent0, parent1):
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


@profile
def main():
    p1 = ["A","E","B","C","G","M","D","H","O","J","K","L","F","N","I"]
    p2 = ["F","D","A","N","K","H","L","M","I","G","J","E","B","C","O"]

    for i in range(1000):
        order_crossover([x for x in range(1000)], [x for x in range(1000)])

if __name__ == '__main__':
    main()

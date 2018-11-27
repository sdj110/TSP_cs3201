from random import randint
from random import shuffle
from route import Route
from evaluation import calculate_distance

def swap_mutation(mutant):
    """
       Swaps two items in a permutation.
       args:
           list : a route individual
       returns:
           list : the same individual with two items swapped
    """
    first = randint(0, len(mutant)-1)
    second = randint(0, len(mutant)-1)
    while (second == first):
        second = randint(0, len(mutant)-1)
    mutant[first], mutant[second] = mutant[second], mutant[first]
    return Route(mutant)

def reverse_mutation(mutant):
    """
       Reverses a segment of a permutation.
       args:
           list : a route individual
       returns:
           list : the same individual with a segment reversed
    """
    first = randint(0, len(mutant)-1)
    second = randint(0, len(mutant))
    while (second == first):
        second = randint(0, len(mutant))
    mutant[first:second] = reversed(mutant[first:second])
    return Route(mutant)

def scramble_mutation(mutant):
    """
       Scrambles a segment of a permutation.
       args:
           list : a route individual
       returns:
           list : the same individual with a segment scrambled
    """
    first = randint(0, len(mutant)-1)
    second = randint(0, len(mutant))
    while (second == first):
        second = randint(0, len(mutant))
    copy = mutant[first:second]
    shuffle(copy)
    mutant[first:second] = copy
    return Route(mutant)

def heuristic_swap(individual):
    """
       Swaps two items in a permutation, while attempting to preserve desirable
       subpaths.
       args:
           list : a route individual
       returns:
           list : the same individual with two items swapped
           boolean : whether to switch to regular swap mutation
    """
    mutant = individual.get_cities()
    city_ids = individual.get_city_ids()
    fitness = individual.get_fitness()
    threshold = fitness / (len(mutant) * 2)
    reject = True
    while reject:
        reject = False
        first = randint(0, len(mutant)-1)
        second = randint(0, len(mutant)-1)
        while (second == first):
            second = randint(0, len(mutant)-1)
        firstFit = calculate_distance(mutant[first], mutant[(first+1) % len(mutant)])
        firstFit += calculate_distance(mutant[first], mutant[(first-1) % len(mutant)])
        firstFit /= 2
        if (firstFit < threshold):
            reject = True
            continue
        secondFit = calculate_distance(mutant[second], mutant[(second+1) % len(mutant)])
        secondFit += calculate_distance(mutant[second], mutant[(second-1) % len(mutant)])
        secondFit /= 2
        if (secondFit < threshold):
            reject = True
    city_ids[first], city_ids[second] = city_ids[second], city_ids[first]
    return Route(city_ids)

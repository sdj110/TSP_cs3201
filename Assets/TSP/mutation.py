from random import randint
from random import shuffle
from route import Route

def swap_mutation(individual):
    """
       Swaps two items in a permutation.
       args:
           list : a route individual
       returns:
           list : the same individual with two items swapped
    """

    mutant = individual.get_cities()
    first = randint(0, len(mutant)-1)
    second = randint(0, len(mutant)-1)
    while (second == first):
        second = randint(0, len(mutant)-1)
    mutant[first], mutant[second] = mutant[second], mutant[first]
    return Route(mutant, False)

def reverse_mutation(individual):
    """
       Reverses a segment of a permutation.
       args:
           list : a route individual
       returns:
           list : the same individual with a segment reversed
    """

    mutant = individual.get_cities()
    first = randint(0, len(mutant)-1)
    second = randint(0, len(mutant))
    while (second == first):
        second = randint(0, len(mutant))
    mutant[first:second] = reversed(mutant[first:second])
    return Route(mutant, False)

def scramble_mutation(individual):
    """
       Scrambles a segment of a permutation.
       args:
           list : a route individual
       returns:
           list : the same individual with a segment scrambled
    """

    mutant = individual.get_cities()
    first = randint(0, len(mutant)-1)
    second = randint(0, len(mutant))
    while (second == first):
        second = randint(0, len(mutant))
    copy = mutant[first:second]
    shuffle(copy)
    mutant[first:second] = copy
    return Route(mutant, False)

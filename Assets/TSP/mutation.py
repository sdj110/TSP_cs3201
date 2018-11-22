from random import randint
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


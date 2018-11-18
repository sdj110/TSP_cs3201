from random import randint

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
    if (second == first):
        second = (second + 1) % len(mutant)
    mutant[first], mutant[second] = mutant[second], mutant[first]


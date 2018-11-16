from route import Route
from random import randint

def tournament_selection(population, mating_pool_size, tournament_size):
    """
        Select parents for the mating pool using tournament selection
        with replacement.
        args:
            list : the population of routes
            int  : the size of the mating pool
            int  : the size of each tournament
        returns:
            list : the selected mating pool
    """

    selected = []
    current_parent = 0
    while (current_parent < mating_pool_size):
        # Tournament is a list of indices
        tournament = []
        while (len(tournament) < tournament_size):
            competitor = randint(0, len(population) - 1)
            tournament.append(competitor)
        winner = tournament[0]
        for i in tournament:
            if (population[i].get_fitness() > population[winner].get_fitness()):
                winner = i
        # Mating pool is a list of route objects
        selected.append(population[winner])
        current_parent = current_parent + 1

    return selected

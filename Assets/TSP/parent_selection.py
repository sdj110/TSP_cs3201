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
            if (population[i].get_fitness() < population[winner].get_fitness()):
                winner = i
        # Mating pool is a list of route objects
        selected.append(population[winner])
        current_parent = current_parent + 1
    return selected

def multi_winner_tourney_selection(population, mating_pool_size, tournament_size, tournament_winners):
    """
        Selects parents for the mating pool using larger tournament sizes
        and multiple winners.
        args:
            list : the population of routes
            int  : the size of the mating pool
            int  : the size of each tournament
            int  : how many individuals get out of the tourney
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
        winners = []
        for i in range(tournament_winners): #initialize the winners with sample data
            winners.append(tournament[0])
        for j in tournament:
            winners.append(j) #add the candidate to the end of the winners list
            winners = sort_winners(population, winners, len(winners)-1) #sort the winners, removing the worst one
        for k in winners:
            selected.append(population[k])
        current_parent = current_parent + tournament_winners
    # ensure that the mating pool is the correct size 
    while current_parent > mating_pool_size:
        selected.pop(len(selected)-1)
        current_parent -= 1
    return selected

def sort_winners(population, winners, competitor_loc):
    #return condition: competitor is the best
    if competitor_loc == 0: 
        winners.pop()
        return winners
    #return condition: competitor isn't better than the next individual
    elif population[winners[competitor_loc]].get_fitness() <= population[winners[competitor_loc-1]].get_fitness():
        winners.pop()
        return winners
    #recursion condition: competitor is still better than the next individual
    elif population[winners[competitor_loc]].get_fitness() > population[winners[competitor_loc-1]].get_fitness():
        competitor = winners[competitor_loc]
        winners[competitor_loc] = winners[competitor_loc-1] #swap the competitor with the worse individual
        winners[competitor_loc-1] = competitor
        return sort_winners(population, winners, competitor_loc-1) #recursion
from route import Route
import city_manager

def permutation (pop_size):
    """
        Initialize the population as a permutation of the set of all cities.
        args:
            pop_size : int
        returns:
            list of Routes
    """
    population = []
    for i in range(pop_size):
        population.append(Route(city_manager.create_tour()))
    return population

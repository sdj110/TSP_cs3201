from route import Route

## TODO: A good heuristic here would be ideal.
def permutation (pop_size, cities):
    """
        Initialize the population as a permutation  of the set of all cities.
        args:
            pop_size : int
            cities : List of City objects
        returns:
            list of cities
    """
    population = []
    for i in range(pop_size):
        population.append(Route(cities))
    return population

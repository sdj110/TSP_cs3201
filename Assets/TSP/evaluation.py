

def TSP_fitness(individual):
    """
        Calculate fitness value based on distance between cities in the individual.
        args:
            list : list of cities
        returns:
            float : sum of distances between each city
    """
    distance = 0
    for x in range(len(individual)):
        distance += individual[x].calculate_distance(individual[(x+1) % len(individual)].position)
    return distance


from math import hypot

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
        distance += calculate_distance(individual[x], individual[(x+1) % len(individual)])
    return distance

def calculate_distance(city1, city2):
        """
            Returns the euclidean distance from this city and another city.
            args:
                city1: tuple representing the first cities x,y coords
                city2: tuple representing the second cities x,y coords
            returns:
                float : the cities distance. 
        """
        return hypot(city1[0] - city2[0], city1[1] - city2[1])

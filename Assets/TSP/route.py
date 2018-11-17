
from numpy import random
from evaluation import TSP_fitness

class Route:
    def __init__(self, city_list, use_permutation=True):
        """
            Constructer creates new permutation and sets its list of cities and fitness.
        """
        if use_permutation:
            self.cities = random.permutation(city_list).tolist()
        else:
            self.cities = city_list
        self.calculate_fitness()
    
    def get_cities(self):
        """
            Returns a list containing all cities within this permutation.
        """
        return self.cities

    def get_fitness(self):
        """
            Returns the fitness value of this permutation.
        """
        return self.fitness

    def calculate_fitness(self):
        """
            Calculate the fitness of this permutation.
            returns:
                float : fitness value
        """
        self.fitness = int(TSP_fitness(self.cities))
        return self.fitness

    def __str__(self):
        return str(self.cities)

    def __repr__(self):
        return str(self.cities)
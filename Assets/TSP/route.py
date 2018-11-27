
from evaluation import TSP_fitness
from city_manager import generate_tour
from copy import deepcopy

class Route:
    def __init__(self, city_list):
        """
            Constructer creates new permutation and sets its list of cities and fitness.
        """
        self.cities = city_list
        self.calculate_fitness()
    
    def get_cities(self):
        """
            Returns a list containing all cities within this permutation.
        """
        return generate_tour(self.cities)

    def get_city_ids(self):
        """
            returns a list of each cities id.
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
        self.fitness = int(TSP_fitness(self.get_cities()))
        return self.fitness

    def create_copy(self):
        return deepcopy(self)

    def __str__(self):
        return str(self.cities)

    def __repr__(self):
        return str(self.cities)

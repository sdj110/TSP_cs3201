class Route:
    def __init__(self, cities, fitness):
        """
            Constructer creates new permutation and sets its list of cities and fitness.
        """
        self.cities = []
        self.fitness = -1   # default to -1 so we can gurantee it hasn't yet been calculated
    
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

    def add_city(self, City):
        """
            Adds a provided City object to the list of cities.
            args:
                City : City object containing its coordinates.
        """
        self.cities.append(City)

    def calculate_fitness(self):
        """
            Calculate the fitness of this permutation.
        """
        self.fitness = -1 # TODO: call the evaluation function here once completed
from math import hypot

class City:
    def __init__(self, x, y):
        """
            Constructor creates new city and sets position attributes.
            args:
                x : float
                y : float
        """
        self.position = (x, y)
    
    def get_position(self): 
        """
            Returns tuple representing cities position in tour.
        """
        return self.position
    
    def calculate_distance(self, pos):
        """
            Returns the euclidean distance from this city and another city.
            since tours are permutations of the set of all cities, direction
            is not considered, therefore always returns abs value of distance.
            args:
                pos : tuple representing another cities position ie P(x, y)
            returns:
                float : the cities distance. 
        """
        return hypot(self.position[0] - pos[0], self.position[1] - pos[1])



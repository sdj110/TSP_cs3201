
from numpy.random import permutation
from math import hypot
import file_manager

CITY_LOOKUP = {}
DISTANCE_DICT = {}
NUM_CITIES = 0

def initialize(filename):
    init_city_dict(filename)
    precompute_distance()

def init_city_dict(filename):
    """
        Read from file and generates a lookup dictionary with key: cityid and 
        value: city coordinates.
    """
    print("Reading cities from file:", filename)
    global NUM_CITIES
    for x in file_manager.read_file(filename):
        data = x.split()
        if data[0] not in CITY_LOOKUP:
            CITY_LOOKUP[int(data[0])] = (float(data[1]), float(data[2]))
            NUM_CITIES += 1
        else:
            print("Key with value", data[0], "already in dict.")

def precompute_distance():
    """
        Loops through each combination of each city and compute their distance. Use this value
        to create DISTANCE_DICT.
    """
    print("Precomputing distance...")
    for i in range(1, NUM_CITIES + 1):
        DISTANCE_DICT[i] = {}

    for i in range(1, NUM_CITIES + 1):
        for j in range(i+1, NUM_CITIES + 1):
            dist = calculate_distance(CITY_LOOKUP[i], CITY_LOOKUP[j])
            DISTANCE_DICT[i][j] = dist
            DISTANCE_DICT[j][i] = dist

def get_distance(city1, city2):
    """
        Look up distance between city1 and city2 in DISTANCE_DICT
        args:
            city1 : int
            city2 : int
    """
    return DISTANCE_DICT[city1][city2]
    
def calculate_distance(city1, city2):
    """
        Use math.hypot to determine Euclidian distance between two points.
        args:
            city1 : tuple
            city2 : tuple
        return:
            float 
    """
    return round(hypot(city1[0] - city2[0], city1[1] - city2[1]), 3)

def generate_tour(cityIds):
    """
        Given a list of city ids returns those cities (x, y) coords
        returns: 
            list of tuples
    """
    coords = []
    for x in cityIds:
        if x in CITY_LOOKUP:
            coords.append(CITY_LOOKUP[x])
    return coords
        
def create_tour():
    """
        Use numpy.random.permutation to generate a permutation of the set [1, NUM_CITIES]
        if city ids.
        returns:
            list of integers
    """
    return permutation([i for i in range(1, NUM_CITIES + 1)]).tolist()

if __name__ == '__main__':
    init_city_dict(file_manager.TEST_PATH)
    print(create_tour())
    




from numpy.random import permutation
import file_manager

CITY_LOOKUP = {}
NUM_CITIES = 0

def init_city_dict(filename):
    """
        Read from file and generates a lookup dictionary with key: cityid and 
        value: city coordinates.
    """
    global NUM_CITIES
    for x in file_manager.read_file(filename):
        data = x.split()
        if data[0] not in CITY_LOOKUP:
            CITY_LOOKUP[int(data[0])] = (float(data[1]), float(data[2]))
            NUM_CITIES += 1
        else:
            print("Key with value", data[0], "already in dict.")

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
    



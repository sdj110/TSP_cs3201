
from city import City
import file_manager

def create_cities(filename):
    """
        Reads coordinates from text file and creates list of tuples containing coords.
        returns:
            list : list of tuples
    """
    cities = []
    coords = file_manager.read_pos_from_file(filename)
    for c in coords:  
        cities.append(City(c[0], c[1])) 
    return cities



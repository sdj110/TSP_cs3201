
from city import City
import file_manager

class CityManager:


    def __init__(self):
        """
            Constructor will read from data files and initialize each city.
        """
        self.cities = []

        coords = file_manager.read_pos_from_file(file_manager.SAHARA_PATH)
        for c in coords:  
            self.cities.append(City(c[0], c[1])) 

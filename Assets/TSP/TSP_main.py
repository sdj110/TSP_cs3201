
import file_manager
from city_manager import create_cities
from initialization import permutation


## TODO: figure out what these values should be.
pop_size = 20
mating_pool_size = int(pop_size * 0.5)
tournament_size = 3
mut_rate = 0.1
xover_rate = 0.8
gen_limit = 100

if __name__ == '__main__':
    gen = 0
    ## Create initial population and calculate initial fitness
    population = permutation(pop_size, create_cities(file_manager.TEST_PATH))

    
    
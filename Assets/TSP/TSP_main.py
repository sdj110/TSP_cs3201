
import random as r
import file_manager
from city_manager import create_cities
from initialization import permutation
from recombination import order_crossover
from route import Route
from parent_selection import tournament_selection
from survivor_selection import survivor_selection
from mutation import swap_mutation


## TODO: figure out what these values should be.
pop_size = 20
mating_pool_size = int(pop_size * 0.5)
tournament_size = 3
mut_rate = 0.1
xover_rate = 0.8
gen_limit = 100

if __name__ == '__main__':
    current_gen = 0
    ## Create initial population and calculate initial fitness
    population = permutation(pop_size, create_cities(file_manager.TEST_PATH))
    
    i = 0
    while current_gen < gen_limit:
        parents = tournament_selection(population,mating_pool_size, tournament_size)
        r.shuffle(parents)
        offspring = []
        while len(offspring) < mating_pool_size:
            ## Crossover
            if r.random() < xover_rate:
                off0 = Route(order_crossover(parents[i].get_cities(), parents[i+1].get_cities()), False)
                off1 = Route(order_crossover(parents[i+1].get_cities(), parents[i].get_cities()), False)
            else:
                off0 = Route(population[i].get_cities().copy(), False)
                off1 = Route(population[i+1].get_cities().copy(), False)
            ## mutation
            if r.random() < mut_rate:
                swap_mutation(off0)
                swap_mutation(off1)
            offspring.append(off0)
            offspring.append(off1)
        population = survivor_selection(population, offspring)
        current_gen += 1
    # print the final best solution(s)
    k = 0
    fitness = [x.get_fitness() for x in population]
    for i in range (0, pop_size):
        if fitness[i] == max(fitness):
            print("best solution", k, population[i], fitness[i])
            k = k+1


    


    
    
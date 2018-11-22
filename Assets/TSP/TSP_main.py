
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
pop_size = 100
mating_pool_size = int(pop_size * 0.5)
tournament_size = 4
mut_rate = 0.2
xover_rate = 0.8
gen_limit = 200
staling_limit = 20

if __name__ == '__main__':
    current_gen = 0
    staling = 0
    prevAverage = 0
    ## Create initial population and calculate initial fitness
    population = permutation(pop_size, create_cities(file_manager.SAHARA_PATH))
    while current_gen < gen_limit and staling < staling_limit:
        parents = tournament_selection(population, mating_pool_size, tournament_size)
        r.shuffle(parents)
        offspring = []
        i = 0
        while len(offspring) < mating_pool_size:
            ## Crossover
            if r.random() < xover_rate:
                off0 = Route(order_crossover(parents[i].get_cities(), parents[i+1].get_cities()), False)
                off1 = Route(order_crossover(parents[i+1].get_cities(), parents[i].get_cities()), False)
            else:
                off0 = Route(parents[i].get_cities().copy(), False)
                off1 = Route(parents[i+1].get_cities().copy(), False)
            ## mutation
            if r.random() < mut_rate:
                off0 = swap_mutation(off0)
            if r.random() < mut_rate:
                off1 = swap_mutation(off1)
            offspring.append(off0)
            offspring.append(off1)
            i += 2
        population = survivor_selection(population, offspring)
        print("Generation ", current_gen)
        fitness = [x.get_fitness() for x in population]
        print("Best fitness: ", min(fitness))
        average = sum(fitness)/len(fitness)
        print("Average fitness: ", average)
        if (average == prevAverage):
            staling += 1
        else:
            staling = 0
        prevAverage = average
        current_gen += 1
    # print the final best solution(s)
    if (staling == staling_limit):
        print("Population staled!")
    else:
        print("Gen limit reached!")
    """k = 0
    fitness = [x.get_fitness() for x in population]
    for i in range (0, pop_size):
        if fitness[i] == min(fitness):
            print("best solution", k, fitness[i])
            k = k+1"""


    


    
    

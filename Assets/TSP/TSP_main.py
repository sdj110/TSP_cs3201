
import random as r
import file_manager
from city_manager import create_cities
from initialization import permutation
from recombination import order_crossover
from route import Route
from parent_selection import tournament_selection
from survivor_selection import survivor_selection
from mutation import swap_mutation
from mutation import reverse_mutation
from mutation import scramble_mutation
from mutation import heuristic_swap
from profiler import profile

pop_size = 1000  #must be a multiple of 4
mating_pool_size = int(pop_size * 0.5)
tournament_size = 4
mut_rate = 0.1
xover_rate = 0.9
gen_limit = 10000
staling_limit = 10

@profile
def main():
    current_gen = 0
    staling = 0
    prevAverage = 1
    ## Create initial population and calculate initial fitness
    population = permutation(pop_size, create_cities(file_manager.URUGUAY_PATH))
    stalingThreshold = len(population) * 10
    while current_gen < gen_limit and staling < staling_limit:
        parents = tournament_selection(population, mating_pool_size, tournament_size)
        r.shuffle(parents)
        offspring = []
        i = 0
        while len(offspring) < mating_pool_size:
            ## Crossover
            if r.random() < xover_rate:
                xover_offspring = order_crossover(parents[i].get_cities(), parents[i+1].get_cities())
                off0 = Route(xover_offspring[0], False)
                off1 = Route(xover_offspring[1], False)
            else:
                off0 = Route(parents[i].get_cities().copy(), False)
                off1 = Route(parents[i+1].get_cities().copy(), False)
            ## mutation
            if r.random() < mut_rate:
                off0 = heuristic_swap(off0)
            if r.random() < mut_rate:
                off1 = heuristic_swap(off1)
            offspring.append(off0)
            offspring.append(off1)
            i += 2
        population = survivor_selection(population, offspring)
        fitness = [x.get_fitness() for x in population]
        average = sum(fitness)/len(fitness)

        print("Generation ", current_gen)
        print("Best fitness: ", min(fitness))
        print("Average fitness: ", average)

        if (average/prevAverage > (stalingThreshold-1)/stalingThreshold and average/prevAverage < (stalingThreshold+1/stalingThreshold)):
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


if __name__ == '__main__':
    main()

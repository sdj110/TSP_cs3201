import sys
import random as r
import file_manager
from city_manager import initialize
from initialization import permutation
from recombination import order_crossover
from route import Route
from parent_selection import tournament_selection
from parent_selection import multi_winner_tourney_selection
from survivor_selection import survivor_selection
from mutation import swap_mutation
from mutation import reverse_mutation
from mutation import scramble_mutation
from mutation import heuristic_swap
from datetime import datetime
import summary

pop_size = 1000
mating_pool_size = int(pop_size * 0.5)
tournament_size = 4
mut_rate = 0.1
xover_rate = 0.9
gen_limit = 10000
staling_limit = 10
summaryAvgList = []
summaryBestList = []

def parse_argv():
    if len(sys.argv) <= 1:
        return file_manager.SAHARA_PATH
    cmd = sys.argv[1].lower()
    if cmd == 'u' or cmd == "uruguay":
        return file_manager.URUGUAY_PATH
    elif cmd == 'c' or cmd == "canada":
        return file_manager.CANADA_PATH
    else:
        return file_manager.SAHARA_PATH

def main():
    initialize(parse_argv())
    startTime = datetime.now()
    print("START:")
    current_gen = 0
    staling = 0
    prevAverage = 1

    ## Create initial population and calculate initial fitness
    population = permutation(pop_size)

    useHeuristic = False
    useSwap = False
    staled = False
    heuristicThreshold = len(population) * 0.25
    swapThreshold = len(population) * 5
    stalingThreshold = len(population) * 10
    currentThreshold = heuristicThreshold

    while current_gen < gen_limit and not staled:
        # Switch between tourney and multi-winner-tourney here
        parents = tournament_selection(population, mating_pool_size, tournament_size)
        #parents = multi_winner_tourney_selection(population, mating_pool_size, mw_tournament_size, mw_tournament_winners)
        r.shuffle(parents)
        offspring = []
        i = 0
        while len(offspring) < mating_pool_size:
            ## Crossover
            if r.random() < xover_rate:
                xover_offspring = order_crossover(parents[i].get_city_ids(), parents[i+1].get_city_ids())
                off0 = Route(xover_offspring[0])
                off1 = Route(xover_offspring[1])

            else:
                off0 = parents[i].create_copy()
                off1 = parents[i+1].create_copy()

            ## mutation
            if r.random() < mut_rate:
                if (useSwap):
                    off0 = swap_mutation(off0.get_city_ids())
                elif (useHeuristic):
                    off0 = heuristic_swap(off0)
                else:
                    off0 = scramble_mutation(off0.get_city_ids())

            if r.random() < mut_rate:
                if (useSwap):
                    off1 = swap_mutation(off1.get_city_ids())
                elif (useHeuristic):
                    off1 = heuristic_swap(off1)
                else:
                    off1 = scramble_mutation(off1.get_city_ids())

            ## Add new offspring
            offspring.append(off0)
            offspring.append(off1)
            i += 2
        population = survivor_selection(population, offspring)
        fitness = [x.get_fitness() for x in population]
        average = sum(fitness)/len(fitness)
        bestFit = min(fitness)

        summaryAvgList.append(average)
        summaryBestList.append(bestFit)

        print("Generation ", current_gen)
        print("Best fitness: ", bestFit)
        print("Average fitness: ", average)

        if (average/prevAverage > (currentThreshold-1)/currentThreshold and average/prevAverage < (currentThreshold+1/currentThreshold)):
            staling += 1
        else:
            staling = 0
        if (staling == staling_limit):
            if not useHeuristic:
                useHeuristic = True
                currentThreshold = swapThreshold
                print("Changed from scramble to heuristic swap!")
            elif not useSwap:
                useSwap = True
                currentThreshold = stalingThreshold
                print("Changed from heuristic to random swap!")
            else:
                staled = True
            staling = 0
        prevAverage = average
        current_gen += 1
    # print the final best solution(s)
    if (staled):
        print("Population staled!")
    else:
        print("Gen limit reached!")
    
    endTime = datetime.now()
    deltaT = endTime-startTime
    print("Completed in:", deltaT)
    # output the graphs
    summary.plot_avg_best_fit(summaryAvgList, summaryBestList)
    summary.plot_route(population[fitness.index(min(fitness))])
    summary.visualize()

if __name__ == '__main__':
    main()
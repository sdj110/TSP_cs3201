#summary is meant to generate the average/best fitness writeups, as well as provide the visualizations.

#imports
import numpy as np
import matplotlib.pyplot as plt #this is used for the visualization/graphs

#globals
# (I know these are usually bad, feel free to move them somewhere properly. Just needed a way to not reset them.)
summaryAvgList = []
summaryBestList = []

def avg_fit(population):
    """
        Returns the average fitness of a given population.
    """
    sum = 0
    for x in range(len(population)):
        sum += population[x].get_fitness()
    sum = sum/len(population)   # TODO: maybe ensure that there's only a certain number of decimals here, to keep it looking clean?
    return sum

def best_fit(population):
    """
        Returns the best fitness of a given population.
    """
    lowest = population[0].get_fitness() # set it to the first one so we have something to compare to.
    for y in range(len(population)):
        if population[y].get_fitness() < lowest:
            lowest = population[y].get_fitness()
    return lowest

def generation_avg_best_fit(population):
    """
        Stores the average and best fitness per generation in lists for easy access.
        Run this after every generation is calculated.
    """
    summaryAvgList.append(avg_fit(population))
    summaryBestList.append(best_fit(population))

def summary_avg_best_fit():
    """
        Prints out the final summary of each generation's average and best fitnesses.
        Run this once we've reached the goal.
    """
    #TODO: maybe make some limiter, or only show every 10 or 100 generations... or something.
        #  it's gonna get out of hand pretty quickly printing 10000+ generations or whatever we're doing.
    print("-----")
    print("Final results:")
    for z in range(summaryAvgList):
        print("Generation "+z+": Avg. Fit:", summaryAvgList[z], "Best Fit:", summaryBestList[z])

def visualize_avg_best_fit():   #UNTESTED, will probably break.
    """
        Creates a graph with the average and best fitness plotted over the generations.
        Run this after the goal is reached (and after summary_avg_best_fit() I guess).
    """
    plt.plot(summaryAvgList)
    plt.plot(summaryBestList)
    plt.xlabel("Generation")
    plt.ylabel("Fitness")
    plt.legend()
    plt.show()

#TODO: a general visualizer for the points in a Route and the path taken in them.
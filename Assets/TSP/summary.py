#summary is meant to generate the average/best fitness writeups, as well as provide the visualizations.

#imports
import numpy as np
import matplotlib.pyplot as plt #this is used for the visualization/graphs

def summary_avg_best_fit():
    """
        Prints out the final summary of each generation's average and best fitnesses.
        Run this once we've reached the goal.
    """
    #TODO: maybe make some limiter, or only show every 10 or 100 generations... or something.
        #  it's gonna get out of hand pretty quickly printing 10000+ generations or whatever we're doing.
    print("-----")
    print("Final results:")
#    for z in range(summaryAvgList):
#        print("Generation "+z+": Avg. Fit:", summaryAvgList[z], "Best Fit:", summaryBestList[z])
# ^commented out for now, will refactor/fix variables if we decide to use this.

def visualize_avg_best_fit(sumAvg, sumBest):
    """
        Creates a graph with the average and best fitness plotted over the generations.
        Run this after the goal is reached (and after summary_avg_best_fit() I guess).
    """
    plt.plot(sumAvg)
    plt.plot(sumBest)
    plt.xlabel("Generation")
    plt.ylabel("Fitness")
    plt.legend()    #TODO: get legend working
    plt.show()

#TODO: a general visualizer for the points in a Route and the path taken in them.
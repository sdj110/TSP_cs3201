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

def plot_avg_best_fit(sumAvg, sumBest):
    """
        Creates a graph with the average and best fitness plotted over the generations.
        Run this after the goal is reached or the algorithm stales.
    """
    plt.figure(1) # sets the following lines to all work on the first graph
    plt.plot(sumAvg, label="Average Fitness")
    plt.plot(sumBest, label="Best Fitness")
    plt.xlabel("Generation")
    plt.ylabel("Fitness")
    plt.legend()

def plot_route(bestRoute):
    """
        Creates a graph with the route the best individual took across the points.
        Run this after the goal is reached on the algorithm stales. 
    """
    plt.figure(2) # sets the following lines to all work on the second graph
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plotRoute = bestRoute.get_cities()
    routeLength = len(plotRoute)
    for x in range(routeLength): # loop through all points and draw cities and path
        longitude = plotRoute[x][1]
        latitude = plotRoute[x][0]
        plt.plot(-longitude, latitude, c="k", marker="o", markersize=5, label="Cities")
        
        if x < routeLength-1:
            nextLong = plotRoute[x+1][0] # I know long/lat seem backwards...
            nextLat = plotRoute[x+1][1]  # but I get better results like this??
        else: # if we're at the end of the route, make it go from the end to the start
            nextLong = plotRoute[0][0]
            nextLat = plotRoute[0][1]
        plt.plot((-longitude, -latitude), (nextLong, nextLat)) #play with minus here

def visualize():
    """
        Will display the graphs created by plot_avg_best_fit and plot_route.
        Run this after the two above plot_ functions have been run.
    """
    plt.show()
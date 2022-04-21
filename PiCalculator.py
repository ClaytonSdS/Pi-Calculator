#Author: Clayton Silva dos Santos (github.com/ClaytonSdS)
#coding: utf-8

import random
import numpy as np
import matplotlib.pyplot as plt


class PiCalculator():
    def __init__(self, iterations):
        self.Ni = [] # points in circle
        self.N = [] # all points
        self.iterations = iterations
        self.start_iterations()
        self.set_pi()

    # FUNCTION TO CALCULATE EUCLIDEAN DISTANCE
    def distance(self, point):
        distance = np.sqrt(point[0]**2 + point[1]**2)
        if distance <= 1:
            self.Ni.append(point)
            self.N.append(point)
        else:
            self.N.append(point)

    # FUNCTION TO CREATE RANDOM POINTS -> P = (x,y) x <= 1 and y <=1
    def set_point(self):
        return (random.random(), random.random())

    # CALCULATE PI VALUE
    def set_pi(self):
        self.pi = len(self.Ni) / len(self.N) * 4

    # FUNCTION TO START ITERATIONS
    def start_iterations(self):
        for iterations in range(self.iterations):
            point = self.set_point()
            self.distance(point)


    # PLOT FUNCTION
    def plot(self):
        x_Ni = [self.Ni[i][0] for i in range(len(self.Ni))]
        y_Ni = [self.Ni[i][1] for i in range(len(self.Ni))]
        fig = plt.figure(figsize=(100,100))
        plt.title(f"N = {len(self.N)}; " + r"$N_{i}$ = " + str(len(self.Ni)) + r"; $π$ = " + str(self.pi), fontsize=30)
        plt.scatter(x_Ni, y_Ni, label="$N_{i}$", color="#323335")
        plt.grid(alpha=0.15)
        plt.xlabel("Radius")
        plt.ylabel("Radius")
        plt.legend(loc="upper right", facecolor="#eeeeee")
        plt.savefig(f"pi_plot.jpg", format="jpg", dpi=72)
        plt.close(fig)



# Example
Pi = PiCalculator(10000)

# CHECK THE VALUE OF PI
Pí.pi

# PLOT THE POINTS AMONG THE ITERARIONS
Pi.plot()

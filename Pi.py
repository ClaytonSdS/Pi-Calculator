import random
import numpy as np
import matplotlib.pyplot as plt

class Pi():
    def __init__(self, iterations):
        self.Ni = [] # points in circle
        self.N = [] # all points
        self.No = [] # points out of the circle
        self.iterations = iterations
        self.count = 0

        self.start_iterations()
        self.set_pi()

        #self.plot()

    def distance(self, point):
        distance = np.sqrt(point[0]**2 + point[1]**2)
        if distance <= 1:
            self.Ni.append(point)
            self.N.append(point)
        else:
            self.No.append(point)
            self.N.append(point)

    def set_point(self):
        return (random.random(), random.random())


    def start_iterations(self):

        for iterations in range(self.iterations):
            point = self.set_point()
            self.distance(point)

            if iterations >= 10000000:
                break
            if iterations == self.iterations - 1:
                print(self.iterations)
                self.set_pi()
                self.plot()
                self.count += 1
                self.iterations *= 2
                self.start_iterations()


    def plot(self):
        x_Ni = [self.Ni[i][0] for i in range(len(self.Ni))]
        y_Ni = [self.Ni[i][1] for i in range(len(self.Ni))]

        #x_N = [self.No[i][0] for i in range(len(self.No))]
        y_N = [self.No[i][1] for i in range(len(self.No))]


        #fig.figure(facecolor='red')
        fig = plt.figure(figsize=(100,100))
        #plt.annotate(r'π = $\frac{4N_{i}}{N}$' + f' = {round(self.pi, 7)}', (0.02, 0.9), size=20, bbox=dict(boxstyle="square", fc="#eeeeee", ec="#323335", lw=2))

        plt.title(f"N = {len(self.N)}; " + r"$N_{i}$ = " + str(len(self.Ni)) + r"; $π$ = " + str(self.pi), fontsize=30)

        plt.scatter(x_Ni, y_Ni, label="$N_{i}$", color="#323335")
        #plt.scatter(x_N, y_N, label="$N_{o}$", color="Red")

        plt.grid(alpha=0.15)
        plt.xlabel("Radius")
        plt.ylabel("Radius")
        plt.legend(loc="upper right", facecolor="#eeeeee")

        plt.savefig(f"teste{str(self.count)}.jpg", format="jpg", dpi=72)
        plt.close(fig)


    def set_pi(self):
        self.pi = len(self.Ni)/len(self.N) * 4

a = Pi(1)
a.plot(0)
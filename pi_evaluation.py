import numpy as np
import math
import datetime

class PiEval:
    def __init__(self):
        self.pi = 0
        self.N = 0
        self.method = ""
        self.relerror = 0
        self.abserror = 0
        self.CPUtime = 0
    def deterministic():
        start_time = datetime.datetime.now()
        N = int(input("Enter number of trapezoids: "))
        x = np.linspace(-1,1,N+1)
        area = 0
        for k in range(N):
            a = math.sqrt(1-x[k]**2)
            b = math.sqrt(1-x[k+1]**2)
            area += (x[k+1]-x[k])*(a+b)
        end_time = datetime.datetime.now()
        print("Time taken: ", end_time - start_time)
        return area
    def stochastic():
        start_time = datetime.datetime.now()
        N = int(input("Enter number of stones: "))
        x = np.random.uniform(-1, 1, N)
        y = np.random.uniform(-1, 1, N)

        stones_inside = 0
        stones_outside = 0
        for i in range (0, N):
            if x[i] ** 2 + y[i] ** 2 < 1:
                stones_inside += 1
            else:
                stones_outside += 1

        ratio_of_area = stones_inside / (stones_outside + stones_inside)

        end_time = datetime.datetime.now()
        print("Time taken: ", end_time - start_time)
        return ratio_of_area*4


print(Pi.deterministic())
print(Pi.stochastic())

from question3 import NewtonDescent
import math
import numpy as np

class MonteCarlo(NewtonDescent):

    def __init__(self, start, stepSize):
        super().__init__(start, stepSize)

    # The actual descent implemented in super class

    def step(self, x0):
        x0
        beta = np.random.uniform(0, 2* math.pi)
        x1 = np.array(x0 - self.stepSize * np.array([math.cos(beta), math.sin(beta)]).reshape(2,1), dtype='float64').reshape(2,1)
        decision = self.probability(x1, x0)
        if decision: return x1
        else: return x0

    def probability(self, x1, x0):
        p = np.random.uniform(0,1)
        # add minus
        h = -(self.f(x1[0], x1[1]) - self.f(x0[0], x0[0]))/(10e-5)
        f = np.exp(h)
        if p < f: return True
        else: return False

if __name__ == '__main__':
    monte = MonteCarlo((-2.5, 2), 0.001)
    monte.descent()

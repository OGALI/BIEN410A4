from question2B import GradientDescent
import math
import numpy as np

class MonteCarlo(GradientDescent):

    def __init__(self, start, stepSize):
        super().__init__(start, stepSize)

    def step(self, x0):
        beta = np.random.uniform(0, 2 * math.pi)
        x1 = np.array(x0 - self.stepSize * np.array([math.cos(beta), math.sin(beta)], dtype='float64').reshape(2,1), dtype='float64').reshape(2,1)
        decision = self.probability(x1, x0)
        if decision: return x1
        else: return x0

    def probability(self, x1, x0):
        p = np.random.uniform(0,1)
        f = np.exp(-(self.f(x1[0], x1[1]) - self.f(x0[0], x0[1]))/10e-5)
        if p < f: return True
        else: return False

if __name__ == '__main__':
    monte = MonteCarlo((-2.5, 2), 0.001)
    positions, distances = monte.descent()
<<<<<<< HEAD
    np.save('/Users/alinajmaldin/Desktop/BIEN410A4/output/positions4.npy', positions)  # save
    np.save('/Users/alinajmaldin/Desktop/BIEN410A4/output/distances4.npy', distances)
=======
    np.save('question1/positions4.npy', positions)  # save
    np.save('question1/distances4.npy', distances)
>>>>>>> b20742a2557c3e8c9f1a3540c74cf851d32b238d

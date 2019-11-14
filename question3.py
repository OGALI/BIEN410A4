import numpy as np
import matplotlib.pyplot as plt
from question2B import GradientDescent

class NewtonDescent(GradientDescent):

    # Put all positions in array
    def __init__(self, start, stepSize):
        self.positions = np.array(start, dtype='float64').reshape(1, 2)
        self.stepSize = stepSize
        self.globalMinima = np.array([1, 1], dtype='float64').reshape(2, 1)

    def inverseHessian(self, x, y):
        dxx = self.dxx(x, y)
        dyy = self.dyy(x, y)
        dxy = self.dxy(x, y)
        hessian = np.array([[dxx, dxy], [dxy, dyy]], dtype = 'float64').reshape(2,2)
        inverse_hessian = np.linalg.inv(hessian)
        return inverse_hessian

    def step(self, x0):
        gradient = self.gradient(x=x0[0], y=x0[1])
        inverse_hessian = self.inverseHessian(x=x0[0], y=x0[1])
        x1 = x0 - self.stepSize * np.matmul(inverse_hessian, gradient)
        return x1


if __name__ == '__main__':
    newton = NewtonDescent((-2.5, 2), 0.1)
    positions, distances = newton.descent()

    np.save('question1/positions3.npy', positions) # save
    np.save('question1/distances3.npy', distances)

    plt.plot(positions[:,0], positions[:,1])
    plt.plot(distances)
    plt.show()

import math
import numpy as np
import matplotlib.pyplot as plt


class NewtonDescent():
    f = lambda self, x, y: 100 * math.pow((y - math.pow(x, 2)), 2) + math.pow((1-x), 2)
    # f = lambda self, x, y: 100 * (y - x**2)**2 + (1-x)**2

    dx = lambda self, x, y: 400 * math.pow(x, 3) - 400 * x * y + 2 * x - 2
    dy = lambda self, x, y: 200 * y - 200 * math.pow(x, 2)
    dxx = lambda self, x, y: -400 * y + 400 * math.pow(x, 2) + 800 * math.pow(x, 2) + 2
    dyy = lambda self, x, y: 200
    dxy = lambda self, x, y: -400 * x

    # Put all positions in array
    def __init__(self, start, stepSize):
        self.positions = np.array(start, dtype='float64').reshape(1, 2)
        self.stepSize = stepSize
        self.globalMinima = np.array([1, 1], dtype='float64').reshape(2, 1)

    def gradient(self, x, y):
        dx = self.dx(x, y)
        dy = self.dy(x, y)
        gradient = np.array([dx, dy], dtype = 'float64').reshape(2, 1)
        return gradient

    def inverseHessian(self, x, y):
        dxx = self.dxx(x, y)
        dyy = self.dyy(x, y)
        dxy = self.dxy(x, y)
        hessian = np.array([[dxx, dxy], [dxy, dyy]], dtype = 'float64').reshape(2,2)
        inverse_hessian = np.linalg.inv(hessian)
        return inverse_hessian

    def descent(self):
        # Get starting position
        x0 = np.array((self.positions[0,0], self.positions[0,1]), dtype = 'float64').reshape(2,1)

        dist = np.linalg.norm(x0 - self.globalMinima[0,])

        # Create array of distances
        self.distances = np.array(dist).reshape(1,1)

        while dist > 10e-3:
            x0 = self.step(x0)
            dist = np.linalg.norm(x0 - self.globalMinima[0,])
            self.positions = np.append(self.positions, np.array(x0, dtype=float).reshape(1,2), axis=0)
            self.distances = np.append(self.distances, np.array(dist, dtype=float).reshape(1,1), axis=0)
            print(f'dist: {dist:4.4}; x0: {x0[0]} y0: {x0[1]}')
        return self.positions, self.distances

    # TODO store the distances data and positions
    def step(self, x0):
        gradient = self.gradient(x=x0[0], y=x0[1])
        inverse_hessian = self.inverseHessian(x=x0[0], y=x0[1])
        x1 = x0 - self.stepSize * np.matmul(inverse_hessian, gradient)
        return x1



if __name__ == '__main__':
    newton = NewtonDescent((-2.5, 2), 0.1)
    positions, distances = newton.descent()

    plt.plot(positions[:,0], positions[:,1])
    plt.plot(distances)
    plt.show()

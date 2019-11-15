import sympy as sy
import time
import numpy as np
from scipy.spatial import distance
import math

class GradientDescent():
    def __init__(self, function, start, stepSize):
        self.function = function
        self.positions = np.array([start[0], start[1]], dtype=float).reshape(1,2)
        self.stepSize = stepSize
        self.globalMinima = np.array([1,1], dtype=float).reshape(1,2)

        # Define the derivative symbolically
        x = sy.Symbol('x')
        y = sy.Symbol('y')
        expr = sy.sympify(function)
        self.diffX = sy.diff(expr, x)
        self.diffY = sy.diff(expr, y)


    # Evaluates the function at a point
    def myFunction(self, **kwargs):
        expr = sy.sympify(self.function)
        return expr.evalf(subs=kwargs)


    # Takes the gradient of function at a point
    def Dfunction(self, **kwargs):
        return self.diffX.evalf(subs=kwargs), self.diffY.evalf(subs=kwargs)


    def gradientDescent(self):

        x0, y0 = self.positions[0,0], self.positions[0,1]
        dist = np.linalg.norm(self.positions[0,] - self.globalMinima)
        self.distances = np.array(dist, dtype=float).reshape(1,1)

        while dist > 10e-3:
            gradient = self.Dfunction(x=x0, y=y0)
            x0, y0 = self.step((x0, y0), gradient)
            self.positions = np.append(self.positions, np.array([x0, y0], dtype=float).reshape(1,2), axis=0)
            dist = np.linalg.norm(self.positions[-1,] - self.globalMinima[0,])
            self.distances = np.append(self.distances, np.array(dist, dtype=float).reshape(1,1), axis=0)
            print(f'dist: {dist:5.4}; x0: {x0:5.4}, y0: {y0:5.4}')
        return (self.positions, self.distances)

    def step(self, position, gradient):
        x0, y0 = position[0], position[1]
        gradX, gradY = gradient[0], gradient[1]

        x1 = x0 - self.stepSize*gradX
        y1 = y0 - self.stepSize * gradY
        return (x1, y1)

if __name__ == '__main__':

    optimizer = GradientDescent('100*(y-x^2)^2+(1-x)^2', (-2.5, 2), 0.001)
    positions, distances = optimizer.gradientDescent()

    np.save('/Users/alinajmaldin/PycharmProjects/BIEN410A4/output/positions2.npy', positions) # save
    np.save('/Users/alinajmaldin/PycharmProjects/BIEN410A4/output/distances2.npy', distances)
    # new_num_arr = np.load('data.npy') # load


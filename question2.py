import sympy as sy
import time
import numpy as np
from scipy.spatial import distance
import math

class GradientDescent():
    def __init__(self, function, start, stepSize):
        self.function = function
        self.start = start
        self.stepSize = stepSize

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

        x0, y0 = self.start[0], self.start[1]
        dist = math.sqrt(math.pow((x0-1),2) + math.pow(y0 - 1,2))

        while dist > 10e-3:
            gradient = self.Dfunction(x=x0, y=y0)
            x0, y0 = self.step((x0, y0), gradient)
            dist = math.sqrt(math.pow((x0-1),2) + math.pow(y0 - 1,2))
            print(f'dist: {dist}; x0: {x0}, y0: {y0}')
        return (x0, y0)

    def step(self, position, gradient):
        x0, y0 = position[0], position[1]
        gradX, gradY = gradient[0], gradient[1]

        x1 = x0 - self.stepSize*gradX
        y1 = y0 - self.stepSize * gradY
        return (x1, y1)



optimizer = GradientDescent('100*(y-x^2)^2+(1-x)^2', (-2.5, 2), 0.001)
print(optimizer.gradientDescent())


from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np


fig = plt.figure()
ax = fig.gca(projection='3d')

# Make data
X = np.arange(-50, 50, 0.5)
Y = np.arange(-50, 50, 0.5)
X, Y = np.meshgrid(X, Y)
Z = 100*np.power((Y-np.power(X, 2)), 2) + np.power((1+X), 2)


# Plot the surface.
surf = ax.plot_surface(X, Y, Z, cmap='viridis')
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
plt.title('Plot of $f(x,y) = 100(y - x^2)^2 + (1 + x)^2$')
plt.savefig('question1/question1.jpg', dpi=500)
plt.show()

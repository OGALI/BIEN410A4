import numpy as np
import matplotlib.pyplot as plt

positions2 = np.load('output/positions2.npy')
distances2 = np.load('output/distances2.npy')

positions3 = np.load('output/positions3.npy')
distances3 = np.load('output/distances3.npy')

positions4 = np.load('output/positions4.npy')
distances4 = np.load('output/distances4.npy')


plt.plot(positions2[:,0],positions2[:,1])
plt.title('Position Vectors Obtained After Each Iteration', fontsize=19)
plt.xlabel('X', fontsize=18)
plt.ylabel('Y', fontsize=18)
plt.savefig('output/question2a.jpg', dpi=500)
plt.show(dpi=500)

plt.plot(distances2)
plt.title(' Euclidian Distances Between the position\n vector at each iteration and True Minimum', fontsize=19)
plt.xlabel('Iteration', fontsize=18)
plt.ylabel('Distance', fontsize=18)
plt.savefig('output/question2b.jpg', dpi=500)
plt.show(dpi=500)


plt.plot(positions3[:,0], positions3[:,1])
plt.title('Position Vectors Obtained After Each Iteration', fontsize=19)
plt.xlabel('X', fontsize=18)
plt.ylabel('Y', fontsize=18)
plt.savefig('output/question3a.jpg', dpi=500)
plt.show(dpi=500)

plt.plot(distances3)
plt.title(' Euclidian Distances Between the position\n vector at each iteration and True Minimum', fontsize=19)
plt.xlabel('Iteration', fontsize=18)
plt.ylabel('Distance', fontsize=18)
plt.savefig('output/question3b.jpg', dpi=500)
plt.show(dpi=500)


plt.plot(positions4[:,0], positions4[:,1])
plt.title('Position Vectors Obtained After Each Iteration', fontsize=19)
plt.xlabel('X', fontsize=18)
plt.ylabel('Y', fontsize=18)
plt.savefig('output/question4a.jpg', dpi=500)
plt.show(dpi=500)

plt.plot(distances4)
plt.title(' Euclidian Distances Between the position\n vector at each iteration and True Minimum', fontsize=19)
plt.xlabel('Iteration', fontsize=18)
plt.ylabel('Distance', fontsize=18)
plt.savefig('output/question4b.jpg', dpi=500)
plt.show(dpi=500)

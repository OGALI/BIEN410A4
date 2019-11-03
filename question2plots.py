import numpy as np
import matplotlib.pyplot as plt

positions = np.load('/Users/alinajmaldin/PycharmProjects/BIEN410A4/question1/positions.npy') # save
distances = np.load('/Users/alinajmaldin/PycharmProjects/BIEN410A4/question1/distances.npy')

fig, ax = plt.subplots(2,1)

ax[0].plot(positions[:,0],positions[:,1])
ax[1].plot(distances)
plt.show()


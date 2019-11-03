import numpy as np


positions = np.array([1,2,3,2]).reshape(-1,2)
np.save('/Users/alinajmaldin/PycharmProjects/BIEN410A4/question1/positions.npy', positions) # save

positions = 0
positions = np.load('/Users/alinajmaldin/PycharmProjects/BIEN410A4/question1/positions.npy', positions) # save

print(positions)





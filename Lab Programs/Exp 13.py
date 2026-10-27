import numpy as np

P = np.array([[1, 0], [0, 1]])
C = np.array([[9, 4], [5, 7]])

K = C @ np.linalg.inv(P)
print("Recovered key matrix:")
print(K.astype(int))

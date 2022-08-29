import numpy as np

A = np.array([[1, 2, 3],
			[4, -5, 6],
			[7, 8, 9]])

print("Rank of A:", np.linalg.matrix_rank(A))

print("\nTrace of A:", np.trace(A))

print("\nDeterminant of A:", np.linalg.det(A))

print("\nInverse of A:\n", np.linalg.inv(A))

print("\nMatrix A raised to power 3:\n", np.linalg.matrix_power(A, 3))

print("\nTranspose of A:\n",np.transpose(A))

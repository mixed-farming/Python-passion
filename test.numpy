# We need install numpy in order to import it
import numpy as np

# input two matrices
mat1 = ([1,2,3],[4,5,6],[7,8,9])
mat2 = ([9,8,7],[6,5,4],[3,2,1])

# This will return dot product
res = np.dot(mat1,mat2)

# print resulted matrix
print(res)

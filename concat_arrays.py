import numpy as np

arr1 = np.array([[2, 4], [6, 8]])
arr2 = np.array([[3, 5], [7, 9]])

concat1 = np.concatenate((arr1, arr2), axis=0)
concat2 = np.concatenate((arr1, arr2), axis=1)
concat3 = np.concatenate((arr1, arr2), axis=None)

print(concat1,'\n')
print(concat2,'\n')
print(concat3,'\n')

import numpy as np
# np.random.seed(3) - keeps the rand array intact
arr = np.random.randint(57,157,10)#parameters - (low,high,size,dtype)
print('Array values are : ', arr)

max_element = np.max(arr)
min_element = np.min(arr)

print('maximum element in the array is: ',max_element)
print('minimum element in the array is: ',min_element)

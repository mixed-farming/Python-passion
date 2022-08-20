import numpy as np
def sum_array(arr):
    sum=0
    for i in arr:
        sum = sum + i
    return(sum)

arr=[1,2,3,4,5]
# n=len(arr)
result=sum_array(arr)
print('Sum of the array  : ',result)
print('Numpy array sum : ',np.sum(arr))

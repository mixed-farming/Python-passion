import numpy as np
arr = np.random.randint(1,100,15)#parameters - (low,high,size,dtype)

print("Array is : ",arr)

# calculating length of array
length = len(arr)


# accessing every third element
# from the array
n=5
k=2
print("Array after every k=2nd element access starting from n=5th location")
print(arr[n:length:k])
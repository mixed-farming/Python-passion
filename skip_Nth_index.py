import numpy as np

x=np.array([1,2,3,4,5,6,7,8,9,11,12,13,14,15,16,17,18,19])
n=int(input('Enter the position multiples to be skipped : '))
x_new=[]
count=0

for i in x:
    if(count % n != 0):
        x_new.append(i)
    count+=1

print(x_new)

#x_new = x[np.mod(np.arange(x.size), n) != 0] ---> using numpy modulus method
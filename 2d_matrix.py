def mat_sum(a,n):
    sum=0
    for i in range(0,n,1):
        for j in range(0,n,1):
            sum+=a[i][j]
    return(sum)

def prin_sum(a,n):
    sum=0
    for i in range(0,n,1):
        sum+=a[i][i]
    return(sum)

a = []
n = int(input("Enter the number of row = "))
for i in range(n):
    row = []
    print("Enter the all values for row",i+1,": ")
    for j in range(n):
        row.append(int(input()))
    a.append(row)
print(a)

print(prin_sum(a,3)/mat_sum(a,3))
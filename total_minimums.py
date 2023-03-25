t=int(input()) #number of test cases
for i in range(t):
    n=int(input())
    a=list(map(int,input().split())) #list input
    m=min(a)
    count=sum(1 for x in a if x!=m)
    print(count)

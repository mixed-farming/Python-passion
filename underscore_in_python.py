for _ in range(int(input())): # _ as a throw-away variable
    first=input().split()
    second=input().split()
    count=0
    for i in first:
        count += sum(1 for x in second if x==i)
    print(count) # prints the number of similar elements in both arrays

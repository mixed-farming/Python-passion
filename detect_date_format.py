for _ in range(int(input())):#number of inputs
    s=input()#like 12/05/2023
    d,m,y=s.split('/')
    d=int(d)
    m=int(m)
    if d<=12 and m<=12:
        print('BOTH')
    elif d>12:
        print('DD/MM/YYYY')
    else:
        print('MM/DD/YYYY')

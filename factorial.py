def fac(n):
    fact=1
    for i in range(1,n+1,1):
        fact*=i
    return fact

n=int(input('Enter a number for factorial computation : '))
result=fac(n)
print(n,'! =',result)
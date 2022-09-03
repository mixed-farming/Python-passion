#  swapping two variables with a single statement

a,b,c,e,f = 1,2,3,4,5
print('Before swap : ')
print('a=',a,'\tb=',b,'\tc=',c,'\te=',e,'\tf=',f,'\n\nAfter swap')

a,b,c = c,b,a
e,f = f,e  # single statement swap
print('a=',a,'\tb=',b,'\tc=',c,'\te=',e,'\tf=',f,'\n\n')

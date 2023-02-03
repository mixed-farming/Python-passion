# Given 2nd and 3rd term of a GP, find the nth term to 4th decimal place and print the output as a string

i=float(input("Enter 2nd term of GP: "))
j=float(input("Enter 3rd term of GP: "))
r=j/i
n=int(input("Enter the  number of terms : "))
prod=i
for i in range(0,n-2):
  prod*=r
print(str(round(prod,4)))

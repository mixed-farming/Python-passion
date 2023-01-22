import random

lower="abcdefghijklmnopqrstuvwxyz"
upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits="0123456789"
special="@#$%^&*"

box=lower+upper+digits+special
length=int(input("Provide the length of the password to be generated : "))
password="".join(random.sample(box,length))
print("\nPassword generated :",password)

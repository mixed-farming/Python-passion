from math import sqrt

n = int(input("Enter the number to be checked : "))

# check from 2 to sqrt(n)
# if we found any facto then we can print as not a prime number

# prime_flag maintains status whether the n is prime or not
prime_flag = 0

if n > 1:
    for i in range(2, int(sqrt(n)) + 1):  # default increment is by 1
        if n % i == 0:
            prime_flag = 1
            break
    if prime_flag == 0:
        print("true")
    else:
        print("false")
else:
    print("false")

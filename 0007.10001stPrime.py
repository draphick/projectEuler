#! python3
from math import sqrt

def tenThousandFirstPrime():
    """
        By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
        What is the 10 001st prime number?

        https://projecteuler.net/problem=7

    """
    counter = 0
    thisnum = 1

    def isprime(num):
        for i in range(2, int(sqrt(num)) + 1):
            if (num % i) == 0:
                return False
        else:
            return True
    while counter < 10001:
        thisnum += 1
        if isprime(thisnum) == True:
            counter += 1
    print(counter, thisnum)

tenThousandFirstPrime()


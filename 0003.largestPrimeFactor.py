#! python
import numpy

def largestPrimeNumber(findnum):
    """
        The prime factors of 13195 are 5, 7, 13 and 29.
        What is the largest prime factor of the number 600851475143 ?

        https://projecteuler.net/problem=3

        100 ÷ 2 = 50; save 2
        50 ÷ 2 = 25; save 2
        25 ÷ 2 = 12.5, not evenly so divide by next highest number, 3
        25 ÷ 3 = 8.333, not evenly so divide by try next highest number, 4
        25 ÷ 4 = 6.25, not evenly so divide by try next highest number, 5
        25 ÷ 5 = 5; save 5
        5 ÷ 5 = 1; save 5
    """
    primefactors = []
    for i in range(2,int(findnum/2 + 1)):
        if findnum % i == 0:
            primefactors.append(i)
            continue
        if numpy.prod(primefactors) == findnum:
            break
             
    print(primefactors)

largestPrimeNumber(13195)
largestPrimeNumber(600851475143)

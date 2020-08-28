#! python
from functools import reduce

def sumSquareDiff():
    """
        The sum of the squares of the first ten natural numbers is 1**2 + 2**2 + 3**3 .. + 10**2 = 385
        The square of the sum of the first ten natural numbers is (1+2+3+4..+10) = 55**2 = 3025
        Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640
        Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

        https://projecteuler.net/problem=6

    """

    def getEachSqareRange(a,b):
        return a + b**2 
    def getTotalSquareRange(a,b):
        return a + b
        
    print(reduce(getTotalSquareRange,range(1,101)) ** 2 - reduce(getEachSqareRange,range(1,101)))

sumSquareDiff()


from math import sqrt
from functools import reduce

def thirteenth():
    """
        A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

        a2 + b2 = c2
        For example, 32 + 42 = 9 + 16 = 25 = 52.

        There exists exactly one Pythagorean triplet for which a + b + c = 1000.
        Find the product abc.
        https://projecteuler.net/problem=9

    """
    topnum = 333
    def isperfsquare(num):
        return sqrt(num)


    perfsquares = [sqrt(square)for square in range(1,topnum + 1)[::-1]]
    # perfsquares = [sqrt(square)for square in range(1,topnum + 1)[::-1] if isperfsquare(square)]
    print(perfsquares)
    # for a in perfsquares:
    #     for b in perfsquares:
    #         if a != b:
    #             if a < b:
    #                 c = a + b
    #                 if c in perfsquares:
    #                     # print(a,b,c)
    #                     a = int(sqrt(a))
    #                     b = int(sqrt(b))
    #                     c = int(sqrt(c))
    #                     # print(a, 'squared plus', b, 'squared =', c, 'squared')
    #                     # print('-----')
    #                     # if sum([a,b,c]) == 1000:
    #                     #     print('this')
    #                     break
thirteenth()

 
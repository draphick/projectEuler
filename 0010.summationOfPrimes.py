def amilli(findnum):
    """
        The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
        Find the sum of all the primes below two million.

        https://projecteuler.net/problem=10
    """    
    thisnum = 0
    done = [True] * findnum

    for num in range(2, findnum):
        if done[num]:
            thisnum += num
            for i in range(num*num, findnum, num):
                done[i] = False
    print(thisnum)

amilli(2000000)

 
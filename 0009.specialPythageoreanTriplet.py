from math import sqrt

def thousand():
    """
        A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

        a**2 + b**2 = c**2
        For example, 3**2 + 4**2 = 9 + 16 = 25 = 52.

        There exists exactly one Pythagorean triplet for which a + b + c = 1000.
        Find the product abc.

        https://projecteuler.net/problem=9
    """
    for a in range(1,1000):
        for b in range(1,1000):
            if a != b and a < b:
                total = a ** 2 + b ** 2 
                c = sqrt(total)
                newtotal = sum([a,b,c])
                if c == int(c):
                    newtotal = sum([a,b,int(c)])
                    if newtotal == 1000:
                        answer = (a*b*int(c))
                        print(a,b,int(c))
                        print(a**2,b**2,int(c)**2)
                        print(answer)
                        break
            else:
                pass
thousand()

 
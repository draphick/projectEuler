#! python
import datetime

def smallestMultiple():
    """
        2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
        What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

        https://projecteuler.net/problem=5

        original outpute from this script:
        ['232792560 divided by 20 = 11639628.0', 
        '232792560 divided by 19 = 12252240.0', 
        '232792560 divided by 18 = 12932920.0', 
        '232792560 divided by 17 = 13693680.0', 
        '232792560 divided by 16 = 14549535.0', 
        '232792560 divided by 15 = 15519504.0', 
        '232792560 divided by 14 = 16628040.0', 
        '232792560 divided by 13 = 17907120.0', 
        '232792560 divided by 12 = 19399380.0', 
        '232792560 divided by 11 = 21162960.0', 
        '232792560 divided by 10 = 23279256.0', 
        '232792560 divided by 9 = 25865840.0', 
        '232792560 divided by 8 = 29099070.0', 
        '232792560 divided by 7 = 33256080.0', 
        '232792560 divided by 6 = 38798760.0', 
        '232792560 divided by 5 = 46558512.0', 
        '232792560 divided by 4 = 58198140.0', 
        '232792560 divided by 3 = 77597520.0', 
        '232792560 divided by 2 = 116396280.0', 
        '232792560 divided by 1 = 232792560.0']


        232792560

        This is divisible by all numbers between 1-20
        start:
        2020-08-21 22:25:07.052976
        end
        2020-08-21 22:53:45.575896
    """
    starttime = datetime.datetime.now()
    counter = 100
    multiples = range(1,21)
    divisible = [] 
    while True:
        counter +=1
        for i in multiples[::-1]: 
            if counter % i == 0: 
                answer = counter / i 
                what = str(counter) + " divided by " + str(i) + " = " + str(answer) 
                divisible.append(what) 
                if len(divisible) == 20: 
                    print(divisible) 
                    print(f"\n\n {counter} \n\nThis is divisible by all numbers between 1-20")
                    print('start:')
                    print(starttime)
                    print('end')
                    print(datetime.datetime.now())
                    exit()
            else:
                if len(divisible) > 10: 
                    print(starttime)
                    print(datetime.datetime.now())
                    print(counter,i, len(divisible))
        divisible = [] 
smallestMultiple()


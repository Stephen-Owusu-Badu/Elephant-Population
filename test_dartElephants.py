# Stephanie Taylor
# Fall 2015 CS151 (Science)
# Project 5
# This module tests the dartElephants function in elephant.py

import elephant
import random

def testDarting( pcnt_darted , min_ans , max_ans ):
    calving_interval = 3.1
    juvenile_age = 12
    max_age = 60
    p_calf_survival = 0.85
    p_adult_survival = 0.996
    p_senior_survival = 0.2
    carrying_capacity = 1000000

    params = [calving_interval, pcnt_darted, juvenile_age, max_age, p_calf_survival, p_adult_survival, p_senior_survival, carrying_capacity]

    # Create a new, undarted population
    pop = []
    genders = []
    ages = []
    for i in range( carrying_capacity ):
        # Create a new adult elephant.
        pop.append( [random.choice(['m','f']), random.randint(juvenile_age+1, max_age ), 0, 0] )

    pop = elephant.dartElephants( params, pop )

    numF = 0
    numDarted = 0
    for e in pop:
        if e[0] == 'f':
            numF += 1
            if e[3] == 22:
                numDarted += 1
    print("Darting percentage of %0.3f. It should be around %0.3f, and between %0.3f and %0.3f" % (float(numDarted)/numF,pcnt_darted,min_ans,max_ans))

def main():
    random.seed( 0 )

    # Test the function with a darting percentage of 50%
    print("Test 1")
    testDarting( 0.5 , 0.495 , 0.505 )

    # Test the function with a darting percentage of 0%
    print( "\nTest 2")
    testDarting( 0.0 , 0. , 0. )

    # Test the function with a darting percentage of 100%
    print( "\nTest 3")
    testDarting( 1.0 , 1.0 , 1.0 )
    

if __name__ == '__main__':
    main()

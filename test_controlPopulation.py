# Stephanie Taylor
# Fall 2015 CS151 (Science)
# Project 5
# This module tests the controlPopulation function in elephant.py
# Call it like this:
#    python3 test_controlPopulation.py

import elephant
import random

def testDarting( pcnt_darted , minPerc , maxPerc ):
    calving_interval = 3.1
    juvenile_age = 12
    max_age = 60
    p_calf_survival = 0.85
    p_adult_survival = 0.996
    p_senior_survival = 0.2
    carrying_capacity = 1000000
    num_over = 100

    params = [calving_interval, pcnt_darted, juvenile_age, max_age, p_calf_survival, p_adult_survival, p_senior_survival, carrying_capacity]

    # Create a new, undarted population, and make it too big. It should remain too big if
    # the pcnt_darted > 0
    pop = []
    for i in range( carrying_capacity+num_over ):
        # Create a new adult elephant. 
        pop.append( [random.choice(['m','f']), random.randint(juvenile_age+1, max_age ), 0, 0] )
    (pop, numCulled) = elephant.controlPopulation( params, pop )

    if pcnt_darted > 0.0:
        numF = 0
        numDarted = 0
        for e in pop:
            if e[0] == 'f':
                numF += 1
                if e[3] == 22:
                    numDarted += 1
        print("Darting percentage of %0.3f. It should be around %0.3f and between %0.3f and %0.3f" % (float(numDarted)/numF,pcnt_darted, minPerc, maxPerc))
    else:
        print("Exactly %d should have been culled and %d were" % (num_over, numCulled))

def testCulling( population_overrun , minCalves , maxCalves ):
    calving_interval = 3.1
    juvenile_age = 12
    max_age = 60
    p_calf_survival = 0.85
    p_adult_survival = 0.996
    p_senior_survival = 0.2
    carrying_capacity = 1000000
    pcnt_darted = 0.0

    params = [calving_interval, pcnt_darted, juvenile_age, max_age, p_calf_survival, p_adult_survival, p_senior_survival, carrying_capacity]

    # Create a new, undarted population
    pop = []
    for i in range( carrying_capacity ):
        # Create a new adult elephant. 
        pop.append( [random.choice(['m','f']), random.randint(juvenile_age+1, max_age ), 0, 0] )
    for i in range( population_overrun ):
        # Create a new calf.
        pop.append( [random.choice(['m','f']), 1, 0, 0] )
    (pop,numCulled) = elephant.controlPopulation( params, pop )

    print("Exactly %d should have been culled and %d were" % (population_overrun, numCulled))
    
    # If the population has been properly culled, there will still be calves.
    numCalves = 0
    for e in pop:
        if e[1] == 1:
            numCalves += 1
    print("Out of %d calves before culling, %d remain.  Approximately %d, and between %d and %d should remain." % (population_overrun, numCalves, int((1-float(population_overrun)/(carrying_capacity+population_overrun))*population_overrun), minCalves, maxCalves))

def main():
    random.seed( 0 )

    # Test the function with a darting percentage of 50%
    print("Test 1")
    testDarting( 0.5 , 0.495 , 0.505 )

    # Test the function with a darting percentage of 0%
    print("\nTest 2")
    testDarting( 0.0 , 0.0 , 0.0 )

    # Test the function with a darting percentage of 100%
    print("\nTest 3")
    testDarting( 1.0 , 1.0 , 1.0 )

    # Test the function with a population overrun of 1000
    print("\nTest 4")
    testCulling( 1000 , 995 , 1000 )

    # Test the function with a population overrun of 0
    print("\nTest 5")
    testCulling( 0 , 0 , 0 )

    # Test the function with a population overrun of 10000
    print("\nTest 6")
    testCulling( 10000 , 9870 , 9930 )
    
if __name__ == '__main__':
    main()

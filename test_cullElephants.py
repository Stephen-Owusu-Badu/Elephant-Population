# Stephanie Taylor
# Fall 2015 CS151 (Science)
# Project 5
# This module tests the cullElephants function in elephant.py
# Call it like this:
#    python3 test_cullElephants.py

import elephant
import random

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
    (pop, numCulled) = elephant.cullElephants( params, pop )

    print("We needed to cull exactly %d elephants and exactly %d elephants were culled" % (population_overrun, numCulled))
    
    # If the population has been properly culled, there will still be calves.
    numCalves = 0
    for e in pop:
        if e[1] == 1:
            numCalves += 1
    print( "Out of %d calves before culling, %d remain after culling.  Approximately %d, and between %d and %d should remain." % (population_overrun, numCalves, int((1-float(population_overrun)/(carrying_capacity+population_overrun))*population_overrun), minCalves, maxCalves))
    #return numCalves

def main():
    random.seed( 0 )

    # Test the function with a population overrun of 1000
    print("Test 1")
    testCulling( 1000 , 995 , 1000 )

    # Test the function with a population overrun of 0
    print("\nTest 2")
    testCulling( 0 , 0 , 0 )

    # Test the function with a population overrun of 10000
    print("\nTest 3")
    testCulling( 10000 , 9870 , 9930 )
    
if __name__ == '__main__':
    main()
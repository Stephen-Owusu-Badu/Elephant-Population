# Stephanie Taylor
# Fall 2015 CS151 (Science)
# Project 5
# This module tests the simulateMonth function in elephant.py
# Call it like this:
#    python3 test_simulateYear.py

import elephant
import random

def main():
    random.seed( 0 )

    calving_interval = 3.1
    pcnt_darted = 0.5
    juvenile_age = 12
    max_age = 60
    p_calf_survival = 0.85
    p_adult_survival = 0.996
    p_senior_survival = 0.2
    carrying_capacity = 10000
    params = [calving_interval, pcnt_darted, juvenile_age, max_age, p_calf_survival, p_adult_survival, p_senior_survival, carrying_capacity]

    pop = []
    for i in range( carrying_capacity ):
        pop.append( elephant.newElephant( params, random.randint(juvenile_age+1, max_age ) ) )
        
    mean_1 = 10820
    min_1 = 10730
    max_1 = 10950
    pop = elephant.simulateYear( params, pop )
    print("After 1 year of simulation, there are %d elephants.  There should be around %d and between %d and %d elephants." % (len(pop),mean_1,min_1,max_1))

    mean_2 = 11600
    min_2 = 11450
    max_2 = 11750
    pop = elephant.simulateYear( params, pop )
    print("After 2nd year of simulation, there are %d elephants.  There should be around %d and between %d and %d elephants." % (len(pop),mean_2,min_2,max_2))

if __name__ == '__main__':
    main()

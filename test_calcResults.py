# Stephanie Taylor
# Fall 2015 CS151 (Science)
# Project 5
# This module tests the calcResults function in elephant.py
# Call it like this:
#    python3 test_calcResults.py

import elephant
import random

def main():
    random.seed( 0 )

    calving_interval = 3.1
    pcnt_darted = 0.0
    juvenile_age = 12
    max_age = 60
    p_calf_survival = 0.85
    p_adult_survival = 0.996
    p_senior_survival = 0.2
    carrying_capacity = 10000
    params = [calving_interval, pcnt_darted, juvenile_age, max_age, p_calf_survival, p_adult_survival, p_senior_survival, carrying_capacity]

    min_ages = [1,2,juvenile_age+1,max_age+1]
    max_ages = [1,juvenile_age,max_age,100]

    pop = []
    for pop_idx in range(len(min_ages)):
        for i in range( 10000 ):
            # Create a new elephant in the given age range. It may be male or female
            pop.append( [random.choice(['m','f']), random.randint(min_ages[pop_idx], max_ages[pop_idx] ),0,0 ])
            
    results = elephant.calcResults( params, pop, 10 )
    
    # The order of elements in results should be: numTotal, numCalves, numJuveniles, numFemaleAdults, numMaleAdults, numSeniors, numCulled
    mean_1 = 40000
    print( "There are %d total elephants.  There should be exactly %d" % (results[0],mean_1))
    
    mean_2 = 10
    print( "There are %d elephants culled.  There should be exactly %d" % (results[6],mean_2))
    
    mean_3 = 25.0
    print( "There are %0.2f perc. calves.  There should be exactly %0.2f." % (float(results[1])/results[0]*100,mean_3) )

    mean_4 = 25.0
    print( "There are %0.2f perc. juveniles.  There should be exactly %0.2f." % (float(results[2])/results[0]*100,mean_4) )

    mean_5 = 12.5
    min_5 = 12.0
    max_5 = 13.0
    print( "There are %0.2f perc. adult females.  There should be around %0.2f and between %0.2f and %0.2f." % (float(results[3])/results[0]*100,mean_5,min_5,max_5) )

    mean_6 = 12.5
    min_6 = 12.0
    max_6 = 13.0
    print( "There are %0.2f perc. adult males.  There should be around %0.2f and between %0.2f and %0.2f." % (float(results[4])/results[0]*100,mean_6,min_6,max_6) )

    mean_7 = 25.0
    print( "There are %0.2f perc. seniors.  There should be exactly %0.2f." % (float(results[5])/results[0]*100,mean_7) )
    
if __name__ == '__main__':
    main()

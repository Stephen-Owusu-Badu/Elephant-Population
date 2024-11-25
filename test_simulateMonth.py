# Stephanie Taylor
# Fall 2015 CS151 (Science)
# Project 5
# This module tests the simulateMonth function in elephant.py
# Call it like this:
#    python3 test_simulateMonth.py

import elephant
import random

def countFemalesEligibleForPregnancy( params, pop ):
    numF = 0
    for e in pop:
        gender = e[0]
        age = e[1]
        monthsPregnant = e[2]
        monthsContraceptive = e[3]
        if gender == 'f' and age > params[2] and age <= params[3] and monthsPregnant == 0 and monthsContraceptive == 0:
            numF += 1
    return numF

def countFemalesNewlyPregnant( params, pop ):
    numF = 0
    for e in pop:
        gender = e[0]
        age = e[1]
        monthsPregnant = e[2]
        monthsContraceptive = e[3]
        if gender == 'f' and age > params[2] and age <= params[3] and monthsPregnant == 1:
            numF += 1
    return numF

def countAdultFemales( params, pop ):
    numF = 0
    for e in pop:
        gender = e[0]
        age = e[1]
        monthsPregnant = e[2]
        monthsContraceptive = e[3]
        if gender == 'f' and age > params[2] and age <= params[3]:
            numF += 1
    return numF
    
def main():

    #random.seed( 0 )
    calving_interval = 3.1
    pcnt_darted = 0.5
    juvenile_age = 12
    max_age = 60
    p_calf_survival = 0.85
    p_adult_survival = 0.996
    p_senior_survival = 0.2
    carrying_capacity = 1000000
    params = [calving_interval, pcnt_darted, juvenile_age, max_age, p_calf_survival, p_adult_survival, p_senior_survival, carrying_capacity]

    pop = []
    for i in range( carrying_capacity//4 ):
        # Create a new juvenile or adult male
        pop.append( ['m', random.randint(juvenile_age+1, max_age ) , 0, 0] )
    for i in range( carrying_capacity//4 ):
        # Create a new juvenile or adult female elephant that has been darted
        pop.append( ['f', random.randint(juvenile_age+1, max_age ), 0, random.randint(1,22)] )
    for i in range( carrying_capacity//4 ):
        # Create a new juvenile or adult female elephant that is eligible for pregnancy
        pop.append( ['f', random.randint(juvenile_age+1, max_age ),  0, 0] )
    for i in range( carrying_capacity-3*(carrying_capacity//4) ):
        # Create a new juvenile or adult female elephant that is pregnant
        pop.append( ['f', random.randint(juvenile_age+1, max_age ),  random.randint(1,22), 0] )
    
    # Record the number of elephants that could become pregnant during this
    # second month of simulation. Then we an assess the conception rate.
    numBeforeMonth = len(pop)
    numF = countAdultFemales( params, pop )
    numBreedable = countFemalesEligibleForPregnancy( params, pop )
    pop = elephant.simulateMonth( params, pop )    
    numBabies = len( pop ) - numBeforeMonth
    numNewlyPregnant = countFemalesNewlyPregnant( params, pop )
    mean_1 = 0.0153
    min_1 = 0.0110
    max_1 = 0.0190
    print("Month 1 birth rate of %0.4f. It should be around %0.4f and between %0.4f and %0.4f" % (float(numBabies)/numF,mean_1 ,min_1,max_1))

    mean_2 = 0.0664
    min_2 = 0.0560
    max_2 = 0.0750
    print("Month 1 conception rate of %0.4f. It should be around %0.4f and between %0.4f and %0.4f" % (float(numNewlyPregnant)/numBreedable,mean_2,min_2,max_2))

    # Take into account darting. The above test is on a populations with no contraceptives. but we also want to test the contraception code. 
    pop = elephant.dartElephants( params, pop )
    
    numF = countAdultFemales( params, pop )
    numBreedable = countFemalesEligibleForPregnancy( params, pop )
    pop = elephant.simulateMonth( params, pop )    
    numNewlyPregnant = countFemalesNewlyPregnant( params, pop )
    
    mean_3 = 0.0636
    min_3 = 0.0460
    max_3 = 0.0805
    print("Month 2 conception rate (taking into account darting and only loking at undarted females) of %0.4f. It should be around %0.4f and between %0.4f and %0.4f" % (float(numNewlyPregnant)/numBreedable,mean_3,min_3,max_3))   

if __name__ == '__main__':
    main()
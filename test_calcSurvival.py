# Stephanie Taylor
# Fall 2015 CS151 (Science)
# Project 5
# This module tests the calcSurvival function in elephant.py
# Call it like this:
#    python test_calcSurvival.py

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
    carrying_capacity = 1000000
    params = [calving_interval, pcnt_darted, juvenile_age, max_age, p_calf_survival, p_adult_survival, p_senior_survival, carrying_capacity]

    min_ages = [1,2,max_age+1]
    max_ages = [1,max_age,100]
    age_names = ['calves','juveniles and adults','seniors']
    survival_rates = [p_calf_survival, p_adult_survival, p_senior_survival]

    for pop_idx in range(len(min_ages)):
        pop = []
        for i in range( carrying_capacity ):
            # Create a new elephant in the given age range. It may be male or female
            pop.append( [random.choice(['m','f']), random.randint(min_ages[pop_idx], max_ages[pop_idx] ),0,0 ])
        new_pop = elephant.calcSurvival( params, pop )
        print("%s survival rate of %0.3f. It should be around %0.3f and between %0.3f and %0.3f." % (age_names[pop_idx],float(len(new_pop))/len(pop),survival_rates[pop_idx], survival_rates[pop_idx]-0.002,survival_rates[pop_idx]+0.002))

if __name__ == '__main__':
    main()

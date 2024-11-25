'''
Stephen Owusu Badu
Fall 2024
November 5, 2024.
CS152 Project 08 Extension
This python script simulate the population of elephants over time taking into account 
their darting probability, carrying capacity, age and gender.

To run this program, type the following in the command line
python3 Elephant_extension.py
'''

import random
IDX_calving_interval = 0
IDX_darting_probability = 1
IDX_juvenile_age = 2
IDX_maximum_age = 3
IDX_calf_survival_probability = 4
IDX_adult_survival_probability = 5
IDX_senior_survival_probability = 6
IDX_carrying_capacity = 7
IDX_number_of_years = 8



def createParameterList( darting_probability ):
	'''Creates a list of the parameters with the user specified value 
	for the darting probability, and the default values for everything else'''
		
	
	parameters = [ 0 ] * 9

	
	parameters[ IDX_darting_probability ] = darting_probability

	##Set the default values of all the other parameters in the right spot
	parameters[ IDX_calving_interval ] = 3.1
	parameters[ IDX_juvenile_age ] = 12
	parameters[ IDX_maximum_age ] = 60
	parameters[ IDX_calf_survival_probability ] = 0.85
	parameters[ IDX_adult_survival_probability ] = 0.996
	parameters[ IDX_senior_survival_probability ] = 0.2
	parameters[ IDX_carrying_capacity ] = 1000
	parameters[ IDX_number_of_years ] = 200

	return parameters

class Elephant:
    def __init__(self,gender, age, months_pregnant=0, months_contraceptive_remaining=0):
        self.gender = gender
        self.age = age
        self.months_pregnant = months_pregnant
        self.months_contraceptive_remaining = months_contraceptive_remaining
    '''This function '''
    def incrementAge(self):
        self.age += 1
    '''This function increases months of pregnancy '''
    def increment_pregnancy(self):
        if self.months_pregnant > 0 and self.months_pregnant < 22:
           self.months_pregnant +=1
        elif self.months_pregnant ==22:
            self.months_pregnant = 0
            return True
        return False
    '''This function decreases contraceptive'''
    def decrement_contraceptive(self):
        if self.months_contraceptive_remaining > 0:
            self.months_contraceptive_remaining -= 1
'''This function create new elephant'''
def newElephant(parameters, age):
   
    gender = random.choice(['m', 'f'])
    months_pregnant = 0
    if gender == 'f' and parameters[IDX_juvenile_age] < age <= parameters[IDX_maximum_age]:
        if random.random() < (1 / parameters[IDX_calving_interval]):
            months_pregnant = random.randint(1, 22)
    return Elephant(gender, age, months_pregnant)

'''This function simulate the initial population'''
def initPopulation(parameters):   
    population = []
    for _ in range(parameters[IDX_carrying_capacity]):
        age = random.randint(1, parameters[IDX_maximum_age])
        population.append(newElephant(parameters, age))
    return population

'''This function simulate Month'''
def simulateMonth(parameters, population):
    """Simulate one month in the population, updating pregnancy and contraceptive statuses."""
    new_population = []
    for elephant in population:       
        if elephant.gender == 'f' and elephant.age >= parameters[IDX_juvenile_age]:
            elephant.decrement_contraceptive()           
            if elephant.increment_pregnancy():  
                new_population.append(newElephant(parameters, age=1))          
            if elephant.months_contraceptive_remaining == 0 and elephant.months_pregnant == 0:
                if random.random() < (1.0 / (parameters[IDX_calving_interval] * 12 - 22)):
                    elephant.months_pregnant = 1
        new_population.append(elephant)
    return new_population





parameters = createParameterList(0.5)
population = initPopulation(parameters)
for _ in range(12):  # Simulate a year (12 months)
    population = simulateMonth(parameters, population)


        



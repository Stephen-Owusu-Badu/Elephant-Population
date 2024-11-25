"""
Stephen Owusu Badu
Fall 2024
October 29, 2024
CS152 A Lab and Project 07


Simulating the elephant population in Kruger National Park, South Africa

In this project we developed the simulation step by step creating one function at a time 
and testing it with the provided “test” scripts. 
In the end I had a program which allows me to test 
the effect of different percentages of darting on the total elephant population.

To print this code type the following in the command line:
python3 elephant.py
"""

import random
import sys
import pylab

##Global indices into parameter list
IDX_calving_interval = 0
IDX_darting_probability = 1
IDX_juvenile_age = 2
IDX_maximum_age = 3
IDX_calf_survival_probability = 4
IDX_adult_survival_probability = 5
IDX_senior_survival_probability = 6
IDX_carrying_capacity = 7
IDX_number_of_years = 8

# Indices for elephant attributes
IDXGender = 0
IDXAge = 1
IDXMonthsPregnant = 2
IDXMonthsContraceptiveRemaining = 3

# Accessing elephant attributes
gender = [IDXGender]
age = [IDXAge]
months_pregnant = [IDXMonthsPregnant]
months_contraceptive_remaining = [IDXMonthsContraceptiveRemaining]

# Modifying elephant's age
#age += 1  # Increments age by 1



def createParameterList( darting_probability ):
	'''Creates a list of the parameters with the user specified value 
	for the darting probability, and the default values for everything else'''
		
	##Make an empty list of parameters
	parameters = [ 0 ] * 9

	##Darting probability is user specified
	parameters[ IDX_darting_probability ] = darting_probability

	##Set the default values of all the other parameters in the right spot
	parameters[ IDX_calving_interval ] = 3.1
	parameters[ IDX_juvenile_age ] = 12
	parameters[ IDX_maximum_age ] = 60
	parameters[ IDX_calf_survival_probability ] = 0.85
	parameters[ IDX_adult_survival_probability ] = 0.996
	parameters[ IDX_senior_survival_probability ] = 0.15
	parameters[ IDX_carrying_capacity ] = 1000
	parameters[ IDX_number_of_years ] = 200

	return parameters

parameters = createParameterList(0)  # Darting probability set to 0

print(parameters[IDX_darting_probability])  # Should output 0


def newElephant(parameters, age):
    elephant = [0] * 4
    elephant[IDXGender] = random.choice(['m', 'f'])
    elephant[IDXAge] = age

    # Check if the elephant is female and of breeding age
    if elephant[IDXGender] == 'f' and parameters[IDX_juvenile_age] < age <= parameters[IDX_maximum_age]:
        calving_interval = parameters[IDX_calving_interval]
        if random.random() < (1.0 / calving_interval):
            elephant[IDXMonthsPregnant] = random.randint(1, 22)

    # Initialize contraceptive months as 0
    elephant[IDXMonthsContraceptiveRemaining] = 0
    return elephant

parameters = createParameterList(0)
for _ in range(10):
    print(newElephant(parameters, random.randint(1, parameters[IDX_maximum_age])))

def initPopulation(parameters):
    population = []
    for _ in range(parameters[IDX_carrying_capacity]):
        age = random.randint(1, parameters[IDX_maximum_age])
        population.append(newElephant(parameters, age))
    return population

parameters = createParameterList(0)
population = initPopulation(parameters)
for elephant in population[:10]:  # Print only the first 10 elephants
    print(elephant)

def incrementAge(population):
    for elephant in population:
        elephant[IDXAge] += 1
    return population

parameters = createParameterList(0)
population = initPopulation(parameters)
print("Initial Ages:")
for elephant in population[:10]:  # Print the first 10 elephants' ages before incrementing
    print(elephant[IDXAge])

population = incrementAge(population)
print("\nAges After Incrementing:")
for elephant in population[:10]:  # Print the first 10 elephants' ages after incrementing
    print(elephant[IDXAge])


#Project Code

def calcSurvival(parameters, population):
    # Create an empty list to store elephants that survive
    new_population = []
    
    # Loop over the population list
    for elephant in population:
        #age = elephant[0]  # Assuming each elephant is a dictionary with an 'age' key

        # Determine the survival probability based on age group
        if elephant[IDXAge] == 1:
            survival_prob = parameters[4]
        #elif elephant[IDXAge] <= parameters[IDX_maximum_age] and 2 < IDXAge < 60:
            #survival_prob = parameters[5]

        elif elephant[IDXAge] <= parameters[IDX_maximum_age]:  # Adult
            survival_prob = parameters[IDX_adult_survival_probability]
        else:
            survival_prob = parameters[6]

        # Check if elephant survives to the next year
        if random.random() < survival_prob:
            new_population.append(elephant)  # Add surviving elephant to new_population
    
    return new_population


def dartElephants(parameters, population):
    # Loop over each elephant in the population list
    for elephant in population:
        age = elephant[IDXAge]
        gender = elephant[IDXGender]
        
        # Check if the elephant is a female, within the darting age range
        if gender == 'f' and parameters[IDX_juvenile_age] < age <= parameters[IDX_maximum_age]:
            # Determine if the elephant should be darted based on the darting probability
            print( parameters[IDX_darting_probability] )
            if random.random() < parameters[IDX_darting_probability]:
                # Set pregnancy months to 0 and contraceptive months to 22
                elephant[IDXMonthsPregnant] = 0
                elephant[IDXMonthsContraceptiveRemaining] = 22
    
    return population




def cullElephants(parameters, population):
    # Extract the carrying capacity from parameters
    carrying_capacity = parameters[IDX_carrying_capacity]
    
    # Calculate the number of elephants that need to be culled
    excess_population = len(population) - carrying_capacity

    # Only cull if the population exceeds the carrying capacity
    if excess_population > 0:
        # Shuffle the population to randomly select elephants for culling
        random.shuffle(population)
        
        # Keep only up to the carrying capacity
        new_population = population[:carrying_capacity]
    else:
        # If no culling is needed, retain the current population
        new_population = population
    
    # Return the new population list and the number of elephants culled
    return new_population, max(0, excess_population)

def controlPopulation(parameters, population):
    # Check if darting probability is zero
    if parameters[IDX_darting_probability] == 0:
        # If no darting, call cullElephants and get results
        new_population, num_culled = cullElephants(parameters, population)
    else:
        # If darting probability is greater than zero, call dartElephants
        new_population = dartElephants(parameters, population)
        num_culled = 0  # No elephants are culled when darting

    # Return the updated population and the number of elephants culled
    return new_population, num_culled

import random

def simulateMonth(parameters, population):
    # Create a new list to hold the updated population
    newPop = []

    # Probability of becoming pregnant if not on contraceptives
    pregnancy_probability = 1.0 / (3.1 * 12 - 22)

    # Iterate over each elephant in the population
    for elephant in population:
        # Unpack elephant's attributes for easy access
        gender = elephant[IDXGender]
        age = elephant[IDXAge]
        months_pregnant = elephant[IDXMonthsPregnant]
        contraceptive_months_left = elephant[IDXMonthsContraceptiveRemaining]

        # Check if the elephant is a female adult (older than juvenile age and younger than maximum age)
        if gender == 'f' and age >= parameters[IDX_juvenile_age] :#and age <= parameters[IDX_maximum_age]:
        
            # Decrease months of contraceptive remaining if there is any
            if contraceptive_months_left > 0:
                contraceptive_months_left -= 1

            # Pregnancy logic
            if months_pregnant > 0:
                # Increment months pregnant if it's less than 22 months
                if months_pregnant < 22:
                    months_pregnant += 1
                # If pregnancy reaches 22 months, give birth
                elif months_pregnant == 22:

                    # Call newElephant function to create a calf
                    calf = newElephant(parameters, age=1)  # Assuming newElephant creates a new elephant dictionary
                    newPop.append(calf)  # Add calf to the new population
                    months_pregnant = 0  # Reset pregnancy counter after birth
                
            else:
                # If not pregnant and no contraceptive, check for pregnancy
                if contraceptive_months_left == 0 and random.random() < pregnancy_probability:
                    months_pregnant = 1  # Elephant just became pregnant

        # Update the elephant's status and add to new population
        updated_elephant = [gender, age, months_pregnant, contraceptive_months_left]
        newPop.append(updated_elephant)

    # Return the updated population list
    return newPop


def simulateYear(parameters, population):
    # Step 1: Calculate survival, updating the population
    population = calcSurvival(parameters, population)
    
    # Step 2: Increment age of each elephant in the population
    population = incrementAge(population)
    
    # Step 3: Loop 12 times, simulating each month
    for _ in range(12):
        population = simulateMonth(parameters, population)
    
    # Step 4: Return the updated population list after a year of simulation
    return population

def calcResults(parameters, population, num_culled):

    # Get the juvenile and maximum age limits from parameters
    juvenile_age = parameters[IDX_juvenile_age]
    max_age = parameters[IDX_maximum_age]
    
    # Initialize counters for each demographic category
    num_calves = 0
    num_juveniles = 0
    num_adult_males = 0
    num_adult_females = 0
    num_seniors = 0
    
    # Loop over the population to count each category
    for elephant in population:
        gender = elephant[IDXGender]
        age = elephant[IDXAge]
        
        # Categorize based on age and gender
        if age == 1:
            num_calves += 1
        elif age >=2 and age <= 12:
            num_juveniles += 1
        elif juvenile_age <= age <= max_age:
            if gender == 'f':
                num_adult_females += 1
            else:
                num_adult_males += 1
        else:
            num_seniors += 1
    
    # Calculate the total population
    total_population = len(population)
    
    # Return the results list as specified
    return [total_population, num_calves, num_juveniles, num_adult_males, num_adult_females, num_seniors, num_culled]

def runSimulation(parameters):
    popsize = parameters[IDX_carrying_capacity]

    # Initialize the population
    population = initPopulation(parameters)
    population, numCulled = controlPopulation(parameters, population)

    # Run the simulation for N years, storing the results
    results = []
    for i in range(parameters[IDX_number_of_years]):
        population = simulateYear(parameters, population)
        population, numCulled = controlPopulation(parameters, population)
        results.append(calcResults(parameters, population, numCulled))

        # Check if population is out of control and terminate early if needed
        if results[i][0] > 2 * popsize or results[i][0] == 0:
            print('Terminating early')
            break

    return results


def main(darting_probability):
    # Create the parameter list using the supplied darting probability
    parameters = createParameterList(darting_probability)

    # Run the simulation
    results = runSimulation(parameters)

    # Print the results in a readable format
    print(f"\nDarting Probability: {darting_probability}")
    print("Yearly Simulation Results:")

    
    for year, result in enumerate(results):
        print(f"\nYear {year + 1}:")
        print(f"  Total Population: {result[0]}")
        print(f"  Calves: {result[1]}")
        print(f"  Juveniles: {result[2]}")
        print(f"  Adult Males: {result[3]}")
        print(f"  Adult Females: {result[4]}")
        print(f"  Seniors: {result[5]}")
        print(f"  Elephants Culled: {result[6]}")

    

    
if __name__ == "__main__":
    # Check if a darting probability argument is provided in the command line
    if len(sys.argv) != 2:
        print("Usage: python3 elephant.py <darting_probability>")
        sys.exit(1)
    
    # Convert the darting probability from the command line to a float
    darting_probability = float(sys.argv[1])
    main(darting_probability)


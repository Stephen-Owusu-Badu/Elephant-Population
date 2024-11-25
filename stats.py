'''
stats.py

Stephen Owusu Badu
Fall 2024
CS152 Lab 4

This script contains a collection of basic statistical functions used for data analysis.
These functions are designed to be used with datasets such as the hurricanes.csv file
and are called by other scripts like analyze.py for computing statistics on specified data columns.

To run this program for testing purposes, type the following on the command line:
python3 stats.py
'''
fp = open("hurricanes.csv", "r")
header = fp.readline()
header = header.split(',')
def compute_mean(numbers):
    return sum(numbers) / len(numbers)

def min(data):
    # Initialize min_value to the first element of the list and min_index to 0
    min_value = data[0]
    min_index = 0
    
    # Loop through the list, starting from index 1
    for i in range(1, len(data)):
        # If the current element is smaller than min_value, update min_value and min_index
        if data[i] < min_value:
            min_value = data[i]
            min_index = i
    
    # Return the minimum value and its index
    return min_value, min_index

def max(data):
    # Initialize max_value to the first element of the list and max_index to 0
    max_value = data[0]
    max_index = 0
    
    # Loop through the list, starting from index 1
    for i in range(1, len(data)):
        # If the current element is larger than max_value, update max_value and max_index
        if data[i] > max_value:
            max_value = data[i]
            max_index = i
    
    # Return the maximum value and its index
    return max_value, max_index

def test():
    numbers = [3, 1, 4, 2]
    #return (compute_mean(numbers))  # Should print 2.5
    min_val, min_idx = min(numbers)
    max_val, max_idx = max(numbers)

    
    print(f"Minimum Value: {min_val}, Index: {min_idx}")
    print(f"Maximum Value: {max_val}, Index: {max_idx}")


if __name__ == "__main__":
    test()




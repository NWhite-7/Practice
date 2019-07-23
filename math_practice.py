#####
# Introduction
#####

# This program performs the same simple math using differently coded functions

#####
# Imports
#####

import numpy as np
import random

#####
# Creating random list
#####

# Function to generate list

def generate_random_list():
    random_list = [random.randint(1, 20) for num in range(random.randint(2, 10))]
    return random_list

my_list = generate_random_list()

# Print results

print("Your list is: ", my_list)
print()

#####
# Calculating median
#####

# Function with Boolean expression

def median1(ls):
    sorted_list = sorted(ls)
    if (len(ls) % 2) == 0:
        return (sorted_list[(len(ls) // 2) - 1] + sorted_list[len(ls) // 2]) / 2
    else:
        return sorted_list[(len(ls) - 1) // 2]

# Function with NumPy

def median2(ls):
    return np.median(ls)

# Print results

print('Calculating the median')
print('Manually ', median1(my_list))
print('NumPy: ', median2(my_list))
print()

#####
# Calculating mean
#####

# Function with loop

def mean1(ls):
    sum = 0
    for value in ls:
        sum += value
    mean = sum / len(ls)
    return mean

# Function with different loop

def mean2(ls):
    sum = 0
    for i in range(len(ls)):
        sum += ls[i]
    mean = sum / len(ls)
    return mean

# Function with NumPy

def mean3(ls):
    return np.mean(ls)

# Print results

print('Calculating the mean')
print('Simple loop: ', mean1(my_list))
print('Different loop: ', mean2(my_list))
print('NumPy: ', mean3(my_list))
print()

#####
# Calculating minimum value
#####

# Function with loop

def min1(ls):
    min = ls[0]
    for i in range(len(ls)):
        if ls[i] < min:
            min = ls[i]
    return min

# Function with min

def min2(ls):
    return min(ls)

# Print results

print('Calculating the minimum value')
print('Loop: ', min1(my_list))
print('Built-in function: ', min2(my_list))
print()

#####
# Calculating maximum value
#####

# Function with loop

def max1(ls):
    max = ls[0]
    for i in range(len(ls)):
        if ls[i] > max:
            max = ls[i]
    return max

# Function with max

def max2(ls):
    return max(ls)

# Print results

print('Calculating the maximum value')
print('Loop: ', max1(my_list))
print('Built-in function: ', max2(my_list))
print()

#####
# Sorting a list
#####

# Function to sort manually

def sort1(ls):
    temp_list = [value for value in ls]
    sorted_list = []
    smallest_num = temp_list[0]
    while len(temp_list) > 0:
        for i in range(len(temp_list)):
            if temp_list[i] <= smallest_num:
                smallest_num = temp_list[i]
        sorted_list.append(smallest_num)
        temp_list.remove(smallest_num)
        if len(temp_list) > 0:
            smallest_num = temp_list[0]
    return sorted_list

# Function to sort using sorted

def sort2(ls):
    return sorted(ls)

# Print results

print('Sorting the list')
print('Manually: ', sort1(my_list))
print('Built-in function: ', sort2(my_list))
print()

#####
# Calculating percentiles
#####

# Set desired percentage for calculations

percentage = 25

# Function to calculate manually

def percentile1(ls, value):
    sorted_list = sort2(ls)
    index = ((value / 100) * (len(ls) - 1))
    if (index % 1) == 0:
        percentile = sorted_list[int(index)]
        return percentile
    else:
        split_float = str(index).split('.')
        int_rank1 = int(split_float[0])
        int_rank2 = int(split_float[0]) + 1
        float_rank =  float("0." + split_float[1])
        percentile = (float_rank * (sorted_list[int_rank2] - sorted_list[int_rank1])) + sorted_list[int_rank1]
        return percentile

# Function with NumPy

def percentile2(ls, value):
    return np.percentile(ls, value)

# Print results

print('Calculating percentiles')
print('Manually ({value}th percentile): '.format(value = percentage), percentile1(my_list, percentage))
print('NumPy ({value} percentile): '.format(value = percentage), percentile2(my_list, percentage))
print()

#####
# Performing simple math on each value in list
#####

# Function with simple loop

test = [1, 2, 3]

def add_one1(ls):
    new_list = []
    for value in ls:
        new_list.append(value + 1)
    return new_list

# Function with more complicated loop

def add_one2(ls):
    new_list = []
    for i in range(len(ls)):
        new_list.append(ls[i] + 1)
    return new_list

# Function with list comprehension

def add_one3(ls):
    new_list = [value + 1 for value in ls]
    return new_list

# Function with array

def add_one4(ls):
    new_list = list(np.asarray(ls) + 1)
    return new_list

# Print results

print('Adding one to every value in your list')
print('Original list: ', my_list)
print('Simple loop: ', add_one1(my_list))
print('More complicated loop: ', add_one2(my_list))
print('List comprehension: ', add_one3(my_list))
print('Array conversion: ', add_one4(my_list))
print()

#####
# Introduction
#####

# This program performs the same simple math in a variety of ways

#####
# Imports
#####

import numpy as np
import random

#####
# Define random list
#####

def generate_random_list():
    random_list = [random.randint(1, 20) for num in range(random.randint(2, 10))]
    return random_list

my_list = generate_random_list()

print(my_list)

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

print(add_one1(my_list))

# Function with more complicated loop

def add_one2(ls):
    new_list = []
    for i in range(len(ls)):
        new_list.append(ls[i] + 1)
    return new_list

print (add_one2(my_list))

# Function with list comprehension

def add_one3(ls):
    new_list = [value + 1 for value in ls]
    return new_list

print(add_one3(my_list))

# Function with array

def add_one4(ls):
    new_list = list(np.asarray(ls) + 1)
    return new_list

print(add_one4(my_list))

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

print(median1(my_list))

# Function with np.median

def median2(ls):
    return np.median(ls)

print(median2(my_list))

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

print(mean1(my_list))

# Function with different loop

def mean2(ls):
    sum = 0
    for i in range(len(ls)):
        sum += ls[i]
    mean = sum / len(ls)
    return mean

print(mean2(my_list))

# Function with np.mean

def mean3(ls):
    return np.mean(ls)

print(mean3(my_list))

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

print(min1(my_list))

# Function with min

def min2(ls):
    return min(ls)

print(min2(my_list))

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

print(max1(my_list))

# Function with max

def max2(ls):
    return max(ls)

print(max2(my_list))

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

print(sort1(my_list))

# Function to sort using sorted

def sort2(ls):
    return sorted(ls)

print(sort2(my_list))

#####
# Calculating percentiles
#####

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

print(percentile1(my_list, 25))

# Function with numpy

def percentile2(ls, value):
    return np.percentile(ls, value)

print(percentile2(my_list, 25))

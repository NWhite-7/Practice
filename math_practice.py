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

random_list = [random.randint(1, 20) for num in range(random.randint(2, 20))]
my_list = random_list

print(my_list)

#####
# Performing math on each value in list
#####

# Function with simple loop

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

# List comprehension
def add_one3(ls):
    new_list = [value + 1 for value in ls]
    return new_list

print(add_one3(my_list))

# Array

def add_one4(ls):
    new_array = np.array(ls) + 1
    return new_array

print(add_one4(my_list))

#####
# Calculating median
#####

# Function with Boolean expression

def calculate_median(ls):
    if (len(ls) % 2) == 0:
        return (ls[(len(ls) // 2) - 1] + ls[len(ls) // 2]) / 2
    else:
        return ls[(len(ls) - 1) // 2]

print(calculate_median(my_list))

# Function with np.median

def easy_median(ls):
    return np.median(ls)

print(easy_median(my_list))

#####
# Calculating mean
#####

# Function with loop

def calculate_mean(ls):
    sum = 0
    for value in ls:
        sum += value
    mean = sum / len(ls)
    return mean

print(calculate_mean(my_list))

# Function with different loop

def calculate_mean_2(ls):
    sum = 0
    for i in range(len(ls)):
        sum += ls[i]
    mean = sum / len(ls)
    return mean

print(calculate_mean_2(my_list))

# Function with np.mean

def easy_mean(ls):
    return np.mean(ls)

print(easy_mean(my_list))

#####
# Calculating minimum value
#####

# Function with loop

def minimum_value(ls):
    min = ls[0]
    for i in range(len(ls)):
        if ls[i] < min:
            min = ls[i]
    return min

print(minimum_value(my_list))

# Function with min

def easy_minimum(ls):
    return min(ls)

print(easy_minimum(my_list))

#####
# Calculating maximum value
#####

# Function with loop

def maximum_value(ls):
    max = ls[0]
    for i in range(len(ls)):
        if ls[i] > max:
            max = ls[i]
    return max

print(maximum_value(my_list))

# Function with max

def easy_maximum(ls):
    return max(ls)

print(easy_maximum(my_list))

#####
# Sorting a list
#####

# Function to sort manually

def sort_list(ls):
    sorted_list = []
    smallest_num = ls[0]
    while len(ls) > 0:
        for i in range(len(ls)):
            if ls[i] <= smallest_num:
                smallest_num = ls[i]
        sorted_list.append(smallest_num)
        ls.remove(smallest_num)
        if len(ls) > 1:
            smallest_num = ls[0]
    return sorted_list

print(sort_list(my_list))

# Function to sort using sort

def easy_sort(ls):
    return sorted(ls)

print(easy_sort(my_list))

#####
# Calculating percentiles
#####

# Function without using numpy

def calculate_percentile(ls, value):
    sorted_list = easy_sort(ls)
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

print(calculate_percentile(my_list, 25))

# Function with numpy

def easy_percentile(ls, value):
    return np.percentile(ls, value)

print(easy_percentile(my_list, 25))

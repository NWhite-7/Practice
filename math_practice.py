# Perform the same simple math in a variety of ways.


# Imports
import numpy as np

#####
# Performing math on each value in list
#####

my_list = [1, 2, 3, 4, 5]

# List with loop

new_list1 = []

for value in my_list:
    new_list1.append(value + 1)

print(new_list1)

# List with function

def add_one(ls):
    new_list = []
    for i in range(len(ls)):
        new_list.append(ls[i] + 1)
    return new_list

print (add_one(my_list))

# List comprehension

new_list2 = [value + 1 for value in my_list]

print(new_list2)

# Array

my_array = np.array(my_list)

new_array = my_array + 1

print(new_array)

#####
# Calculating median
#####

my_data1 = [10, 12, 15, 19, 40]
my_data2 = [20, 13, 17, 20, 11, 20]

# Funtion with Boolean expression

def calculate_median(ls):
    if (len(ls) % 2) == 0:
        return (ls[(len(ls) // 2) - 1] + ls[len(ls) // 2]) / 2
    else:
        return ls[(len(ls) - 1) // 2]

print(calculate_median(my_data1))
print(calculate_median(my_data2))

# Function with np.median

def easy_median(ls):
    return np.median(ls)

print(easy_median(my_data1))
print(easy_median(my_data2))

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

print(calculate_mean(my_data1))
print(calculate_mean(my_data2))

# Function with different loop

def calculate_mean_2(ls):
    sum = 0
    for i in range(len(ls)):
        sum += ls[i]
    mean = sum / len(ls)
    return mean

print(calculate_mean_2(my_data1))
print(calculate_mean_2(my_data2))

# Function with np.mean

def easy_mean(ls):
    return np.mean(ls)

print(easy_mean(my_data1))
print(easy_mean(my_data2))

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

print(minimum_value(my_data1))
print(minimum_value(my_data2))

# Function with min

def easy_minimum(ls):
    return min(ls)

print(easy_minimum(my_data1))
print(easy_minimum(my_data2))

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

print(maximum_value(my_data1))
print(maximum_value(my_data2))

# Function with max

def easy_maximum(ls):
    return max(ls)

print(easy_maximum(my_data1))
print(easy_maximum(my_data2))

#####
# Sorting a list
#####

unsorted_list1 = [6, 3, 18, 14, 18]
unsorted_list2 = [13, 2, 5, 2, 10, 9]

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
        if len(ls)>1:
            smallest_num = ls[0]
    return sorted_list

print(sort_list(unsorted_list1))

# Function to sort using sort

def easy_sort(ls):
    return sorted(ls)

print(easy_sort(unsorted_list2))

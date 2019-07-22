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
my_data2 = [11, 13, 17, 20, 20, 20]

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

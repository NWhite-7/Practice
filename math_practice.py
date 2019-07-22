# Imports
import numpy as np

#####
# Performing math on each value
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

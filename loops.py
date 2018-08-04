## MAPPING (taking a collection and building a new collection of the same size)

# from a list 1-50, build a list with those numbers doubled

double_list = []
for x in range(1, 50):
    doubled = x * 2
    double_list.append(doubled)

print(double_list)

# from a list of ['a', 'B', 'C', 'd', 'E', 'F', 'g'], build a list
# where the cases are flipped (upper to lower, lower to upper)

letter_list = ['a', 'B', 'C', 'd', 'E', 'F', 'g']

new_list = []

for x in letter_list:
    if x.islower():
        new_list.append(x.upper())
    elif x.isupper():
        new_list.append(x.lower())

print(new_list)

# from a list ['horse', 'cat', 'trash', 'apriori', 'kevin'],
# and a dictionary {'cat': 3 , 'button': 'fog', 'trash': 'balloons'}
# build a new list, based off the first, where each element is either the
# value corresponding to the key in the dictionary, or Nothing

list1 = ['horse', 'cat', 'trash', 'apriori', 'kevin']
dict1 = {'cat': 3 , 'button': 'fog', 'trash': 'balloons'}
newlist = []

for key in list1:
    if key in dict1:
        newlist.append(dict1[key])
    else:
        newlist.append(None)

print(newlist)

# CATAMORPHISM (destruction) (taking a collection and building a non-collection)

# from a list 1-50, get the sum of all the elements

# from a list 1-50, get the product of all the elements

# from a list [1,6,2,4,2,9,11,4,8], get the maximum element

# from the same list as the above, get the minumum element

# from a list 1-50, get the sum of all the even elements

# FILTERING (taking a collection and returning a collection of the same size or smaller

# from a list 1-50, get a list of just the even elements

# from a list 1-50, get a list of all the elements divisible by 3

# from a list of a-z, get a list of the consenents

# NESTED LOOPS

# for a list of lists of numbers [[1, 2, 3, 4], [60, 61, 62, 63], [101, 102, 103, 104]]
# create a list of lists of only even numbers
# eg: [[2, 4], [60, 62], [102, 104]]

# flattening a nested list. For a list of lists of 10 (1-10, 11-20, 21-30, 31-40, 41-50),
# flatten the list to a list of 1-50

# from the lists a-c, and 1-3, generate a list of their cartesian products.
# (One way to do it would be to build 2-tuples, which would look like:
# [('a',1), ('a',2), ('a',3), ('b',1), ('b',2), ('b',3), ('c',1), ('c',2), ('c',3)]

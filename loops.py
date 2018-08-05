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

total = 0

for num in list(range(1,51)):
    total = total + num

print(total)

# from a list 1-50, get the product of all the elements

total = 1

for num in range(1, 51):
    total = num * total

print(total)

# from a list [1,6,2,4,2,9,11,4,8], get the maximum element (this only works for positive numbers)

mylist = [1,6,2,4,2,9,11,4,8]
max_num = 0

for x in mylist:
    if x > max_num:
        max_num = x

print(max_num) 

# from a list [-1,-6,-2,-4,-2,-9,-11,-4,-8], get the maximum element (if I don't know what's in the list)

mylist = [-1,-6,-2,-4,-2,-9,-11,-4,-8]
max_num = mylist[0]

for x in mylist:
    if x > max_num:
        max_num = x

print(max_num) 


# from the same list as the above, get the minumum element

mylist = [1,6,2,4,2,9,11,4,8]
min_num = mylist[0]

for x in mylist:
    if x < min_num:
        min_num = x

print(min_num)

# from a list 1-50, get the sum of all the even elements

sum_num = 0

for x in range(1, 51):
    if x % 2 == 0:
        sum_num = sum_num + x

print(sum_num)

# FILTERING (taking a collection and returning a collection of the same size or smaller)

# from a list 1-50, get a list of just the even elements

even_list = []

for x in range(1, 51):
    if x % 2 == 0:
        even_list.append(x)

print(even_list)

# from a list 1-50, get a list of all the elements divisible by 3

three_list = []

for x in range(1, 51):
    if x % 3 == 0:
        three_list.append(x)

print(three_list)


# from a list of a-z, get a list of the consonants

import string
alpha_list = list(string.ascii_lowercase[:26])
vowel_list = ['a', 'e', 'i', 'o', 'u']
con_list = []

for x in alpha_list:
    if x not in vowel_list:
        con_list.append(x)

print(con_list)


# NESTED LOOPS

# for a list of lists of numbers [[1, 2, 3, 4], [60, 61, 62, 63], [101, 102, 103, 104]]
# create a list of lists of only even numbers
# eg: [[2, 4], [60, 62], [102, 104]]

lol = [[1, 2, 3, 4], [60, 61, 62, 63], [101, 102, 103, 104]]
lol1 = []
lol2 = []
lol3 = []

for x in lol[0]:
    if x % 2 == 0:
        lol1.append(x)

for x in lol[1]:
    if x % 2 == 0:
        lol2.append(x)

for x in lol[2]:
    if x % 2 == 0:
        lol3.append(x)

lol_even = [(lol1), (lol2), (lol3)]

print(lol_even)

#----- Above is not the right way -----

lol = [[1, 2, 3, 4], [60, 61, 62, 63], [101, 102, 103, 104]]

output = []

for one_list in lol:
    evens = []
    for x in one_list:
        if x % 2 == 0:
            evens.append(x)
    output.append(evens)

print(output)

# flattening a nested list. For a list of lists of 10 (1-10, 11-20, 21-30, 31-40, 41-50),
# flatten the list to a list of 1-50

lol10 = [list(range(1,11)), list(range(11,21)), list(range(21,31)), list(range(31,41)), list(range(41,51))]
flattest_list = []

for a_list in lol10:
    for x in a_list:
        flattest_list.append(x)

print(flattest_list) 


# from the lists a-c, and 1-3, generate a list of their cartesian products.
# (One way to do it would be to build 2-tuples, which would look like:
# [('a',1), ('a',2), ('a',3), ('b',1), ('b',2), ('b',3), ('c',1), ('c',2), ('c',3)]

x_list = ['a', 'b', 'c']
y_list = [1, 2, 3]

combo_list = []

for x in x_list:
    for y in y_list:
        combo_list.append((x, y))

print(combo_list)

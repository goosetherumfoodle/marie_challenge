## MAPPING (taking a collection and building a new collection of the same size)

# from a list 1-50, build a list with those numbers doubled

# from a list of ['a', 'B', 'C', 'd', 'E', 'F', 'g'], build a list
# where the cases are flipped (upper to lower, lower to upper)

# from a list ['horse', 'cat', 'trash', 'apriori', 'kevin'],
# and a dictionary {'cat': 3 , 'button': 'fog', 'trash': 'balloons'}
# build a new list, based off the first, which each element either the
# value corresponding to the key in the dictionary, or Nothing

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

#

# from the lists a-c, and 1-4, generate a list of their cartesian product.
# (One way to do it would be to build 2-tuples, which would look like:
# [('a',1), ('a',2), ('a',3), ('b',1), ('b',2), ('b',3), ('c',1), ('c',2), ('c',3)]


# def myFun():{
#     horse = 3
# }

# horse + 5


outerNum = 5

def add(innerNum):
    return innerNum + outerNum

add(2)
# => 7

add(10)

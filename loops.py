## MAPPING

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
"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 2
SUPERLIST = 3
EQUAL = 1
UNEQUAL = 0

def sublist(list_one, list_two):
    if list_one == list_two or (not list_one and not list_two):
        return EQUAL
    if len(list_one) < len(list_two):
        if check_sublist(list_one, list_two):
            return SUBLIST
    if len(list_one) > len(list_two):
        if check_sublist(list_two, list_one):
            return SUPERLIST
    return UNEQUAL
        
def check_sublist(smaller_list, bigger_list):
    if not smaller_list:
        return True
    # The for loop below checks each value in the bigger list. If one value matches with the first element in the smaller list
    # then the bigger list is broken down into a smaller list having the same length as the smaller list. This maintains the order.
    # Finally this smaller list from the bigger list is checked with the original smaller list.
    for index, value in enumerate(bigger_list):
        if value == smaller_list[0]:
            if smaller_list == bigger_list[index: index + len(smaller_list)]:
                return True
    return False
    

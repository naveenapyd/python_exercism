def append(list1, list2):
    return list1 + list2

def concat(lists):
    final_list = []
    for index in range(len(lists)):
        final_list += lists[index]
    return final_list

def filter(function, list):
    final_list = []
    for value in list:
        if function(value):
            final_list += [value]
    return final_list

def length(list):
    sum = 0
    for value in list:
        sum += 1
    return sum

def map(function, list):
    final_list = []
    for value in list:
        final_list += [function(value)]
    return final_list

def foldl(function, list, initial):
    result = initial
    for value in list:
        result = function(result, value)
    return result

def foldr(function, list, initial):
    result = initial
    for value in reverse(list):
        result = function(result, value)
    return result

def reverse(list):
    final_list = []
    if len(list) == 0:
        return final_list
    for index in range(len(list)-1, -1, -1):
        final_list += [list[index]]
    return final_list
        

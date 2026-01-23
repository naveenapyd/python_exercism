def flatten(iterable):
    # recursive function
    flat_list = []
    for value in iterable:
        if value == None:
            # the iterable that needs to be stored in the flat_list are the numbers
            continue
        # check if each value in the list is another list or not
        if isinstance(value, list):
            # if its a list, then call the function again to open the inner list
            flat_list.extend(flatten(value))
        else:
            # when it is not a list and just a value, simply add the value to the new list
            flat_list.append(value)
    return flat_list

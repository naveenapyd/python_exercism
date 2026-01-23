def flatten_helper(iterable):
    for value in iterable:
        # using 'yield' pauses the function at the previous iteration
        # does not start a new loop from the 0th iteration again
        # as the for loop from the below function runs
        if isinstance(value, list):
            # checks if the value is a list
            yield from flatten_helper(value)
            # takes the values from the inner list - yields all the values from the inner list
        elif value is not None:
            # checks the values if they are not a list - yields the value and sends to 'val' in the below function
            yield value
            
def flatten(iterable):
    flat_list = []
    for val in flatten_helper(iterable):
        # calls the yield fn
        # the yield value will come to 'val' and the above function will get paused
        # this 'val' will get appended
        # and when the second yield happens, that value will come to 'val' next, and so on
        flat_list.append(val)
    return flat_list
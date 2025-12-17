def square_root(number):
    if number < 0:
        raise ValueError('Square root can be calculated for only positive numbers.')
    lower_bound = 1
    upper_bound = number
    while lower_bound <= upper_bound:
        midpoint = (lower_bound + upper_bound) // 2 
        # midpoint of a range of values is nothing but the median of the data
        # here only natural numbers are considered
        midpoint_square = midpoint * midpoint
        if midpoint_square == number:
            return midpoint
        elif midpoint_square > number:
            upper_bound = midpoint - 1
        elif midpoint_square < number:
            lower_bound = midpoint + 1

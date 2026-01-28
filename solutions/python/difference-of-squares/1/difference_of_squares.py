def square_of_sum(number):
    sum = 0
    value = 1
    while value <= number:
        sum += value
        value += 1
    return sum * sum

def sum_of_squares(number):
    sum = 0
    value = 1
    square = 1
    while value <= number:
        square = value * value
        sum += square
        value += 1
    return sum

def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)

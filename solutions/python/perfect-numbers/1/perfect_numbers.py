def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")
    sum_f = sum_of_factors(number)
    if sum_f == number:
        return 'perfect'
    if sum_f > number:
        return 'abundant'
    if sum_f < number:
        return 'deficient'
    
def sum_of_factors(number):
    n = 1
    sum = 0
    while n < number:
        if number % n == 0:
            sum += n
        n += 1
    return sum
        

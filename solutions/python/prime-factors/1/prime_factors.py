def factors(value):
    prime_factors = []
    if value == 1:
        return prime_factors
    if value == 2:
        prime_factors.append(value)
        return prime_factors
    divisor = 2
    while divisor <= value:
        # checking till the root of the number as it can't be more than root
        # this won't work for prime numbers 
        while value % divisor == 0:
            prime_factors.append(divisor)
            value //= divisor
        # the next step should be outside the inner loop 
        # so that it will check for repetitions as well, i.e., in case of 4, 2 needs to be checked twice
        if divisor == 2:
            divisor += 1
        # 2 is the only even prime number, so after 2 all the other even numbers can be skipped
        else:
            divisor += 2 
    return prime_factors
        

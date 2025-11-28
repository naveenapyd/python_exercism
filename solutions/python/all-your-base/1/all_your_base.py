def rebase(input_base, digits, output_base):
    if input_base < 2:
        raise ValueError('input base must be >= 2')
    if output_base < 2:
        raise ValueError('output base must be >= 2')
    for value in digits:
        if value < 0 or value >= input_base:
            raise ValueError('all digits must satisfy 0 <= d < input base')
    number_in_base_10 = 0
    for index, value in enumerate(digits):
        number_in_base_10 += value * pow(input_base, len(digits) - index - 1)
    number = []
    dividend = number_in_base_10
    if dividend == 0:
        return [0]
    while dividend > 0:
        quotient = dividend // output_base
        number.append(dividend % output_base)                
        dividend = quotient
    number.reverse()
    return number
    
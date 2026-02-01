def egg_count(display_value):
    # display_value is a decimal number
    # convert this to binary number
    # count the number of 1s in the binary number
    reversed_binary_number = ''
    while display_value > 0:
        remainder = display_value % 2
        reversed_binary_number += str(remainder)
        display_value //= 2
    sum = 0
    for value in reversed_binary_number:
        if value == '1':
            sum += 1
    return sum

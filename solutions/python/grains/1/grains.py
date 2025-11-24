def square(number):
    if (number >= 1 and number <= 64):
        return 2 ** (number-1)
    raise ValueError("square must be between 1 and 64")

def total():
    count = 64
    total_grains = 0
    while (count > 0):
        total_grains = total_grains + square(count)
        count -= 1
    return total_grains
    

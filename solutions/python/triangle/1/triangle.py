def lengths_of_sides(sides):
    return sides[0] > 0 and sides[1] > 0 and sides[2] > 0

def sum_of_lengths(sides):
    return (sides[0] + sides[1] >= sides[2]) and (sides[1] + sides[2] >= sides[0]) and (sides[2] + sides[0] >= sides[1])
        
def equilateral(sides):
    return lengths_of_sides(sides) and sum_of_lengths(sides) and (sides[0] == sides[1] == sides[2])

def isosceles(sides):
    return lengths_of_sides(sides) and sum_of_lengths(sides) and ((sides[0] == sides[1]) or (sides[1] == sides[2]) or (sides[2] == sides[0]))

def scalene(sides):
    return lengths_of_sides(sides) and sum_of_lengths(sides) and (sides[0] != sides[1] and sides[1] != sides[2] and sides[2] != sides[0])

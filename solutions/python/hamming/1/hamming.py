def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError('Strands must be of equal length.')
    if len(strand_a) == 0:
        return 0
    sum = 0
    for index_a, char_a in enumerate(strand_a):
        for index_b, char_b in enumerate(strand_b):
            if index_a == index_b and char_a == char_b:
                sum += 1
    return len(strand_a) - sum

def rows(letter):
    alphabet_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for index, char in enumerate(alphabet_upper):
        # consider only upper triangle till the input 'letter'
        if char == letter:
            letters_to_consider = alphabet_upper[:index + 1]

    if len(letters_to_consider) == 1:
        return list(letters_to_consider)

    diamond = []

    for index, char in enumerate(letters_to_consider):
        if index == 0:
            # only first row will have one letter, other rows will have two letters
            first_row = ' '*(len(letters_to_consider)-1) + char + ' '*(len(letters_to_consider)-1)
            diamond.append(first_row)
        else:
            # consider only half string till the letter - left side of the triangle
            # number of spaces before the letter depends on the length of the triangle
            half_row = ' '*(len(letters_to_consider)-index-1) + char
            # half_row can be reversed to get the right side of the triangle; the spaces in between the left and right sides are 2n-1 to get the full row
            full_row = half_row + ' '*(2 * index - 1) + half_row[::-1]
            diamond.append(full_row)
    # upper triangle can simply be reversed by removing the input 'letter' row
    diamond.extend(diamond[len(diamond)-2::-1])
    return diamond

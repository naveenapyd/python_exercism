def rows(letter):
    alphabet_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for index, char in enumerate(alphabet_upper):
        if char == letter:
            letters_to_consider = alphabet_upper[:index + 1]

    if len(letters_to_consider) == 1:
        return list(letters_to_consider)

    diamond = []

    for index, char in enumerate(letters_to_consider):
        if index == 0:
            first_row = ' '*(len(letters_to_consider)-1) + char + ' '*(len(letters_to_consider)-1)
            diamond.append(first_row)
        else:
          half_row = ' '*(len(letters_to_consider)-index-1) + char
          full_row = half_row + ' '*(2 * index - 1) + half_row[::-1]
          diamond.append(full_row)
    diamond.extend(diamond[len(diamond)-2::-1])
    return diamond

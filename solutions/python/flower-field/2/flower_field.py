def annotate(garden):
    if garden == [] or garden == ['']:
        # empty rows and empty columns
        return garden
    new_garden = []
    row_length = len(garden[0])
    for x in range(len(garden)):
        garden_row = ''
        if row_length != len(garden[x]):
            # when lengths of rows are not the same
            raise ValueError('The board is invalid with current input.')
        for y in range(len(garden[0])):
            count = 0
            if garden[x][y] != ' ' and garden[x][y] != '*':
                # when there are characters other than ' ' and '*'
                raise ValueError('The board is invalid with current input.')
            if garden[x][y] == '*':
                garden_row += '*'
            elif garden[x][y] == ' ':
                for x2 in range(x-1, x+2):
                    for y2 in range(y-1, y+2):
                        if x2 == x and y2 == y:
                            # the element for which the check is done should be ignored
                            continue
                        if x2 < 0 or x2 > len(garden)-1:
                            # should be within the range
                            continue
                        if y2 < 0 or y2 > len(garden[0])-1: 
                            # should be within the range
                            continue 
                        if garden[x2][y2] == '*':
                            count += 1
                if count == 0:
                    # when count is zero, it will return zero; it needs to return the empty space
                    garden_row += ' '
                else:
                    # return value is expected to be a list of strings
                    # strings for each row
                    garden_row += str(count)
        new_garden.append(garden_row)
    return new_garden
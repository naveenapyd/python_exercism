def annotate(garden):
    if garden == [] or garden == ['']:
        # empty rows and empty columns
        return garden
    new_garden = []
    row_length = len(garden[0])
    for x in range(len(garden)):
        garden_row = ''
        if row_length != len(garden[x]):
            raise ValueError('The board is invalid with current input.')
        for y in range(len(garden[0])):
            count = 0
            if garden[x][y] != ' ' and garden[x][y] != '*':
                raise ValueError('The board is invalid with current input.')
            if garden[x][y] == '*':
                garden_row += '*'
            elif garden[x][y] == ' ':
                for x2 in range(x-1, x+2):
                    for y2 in range(y-1, y+2):
                        if x2 == x and y2 == y:
                            continue
                        if x2 < 0 or x2 > len(garden)-1:
                            continue
                        if y2 < 0 or y2 > len(garden[0])-1:
                            continue 
                        if garden[x2][y2] == '*':
                            count += 1
                if count == 0:
                    garden_row += ' '
                else:
                    garden_row += str(count)
        new_garden.append(garden_row)
    return new_garden
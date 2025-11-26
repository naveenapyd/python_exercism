def value(colors):
    all_colors = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
    sum = ''
    for one_color in colors[:2]:
        for index, color in enumerate(all_colors):
            if color == one_color:
                sum += str(index)
    return int(sum)

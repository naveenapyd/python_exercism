def label(colors):
    all_colors = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
    metric_prefix = ['ohms', 'kiloohms', 'megaohms', 'gigaohms']
    number = ''
    trailing_zeros = 0
    for one_color in colors[:2]:
        for index, each_color in enumerate(all_colors):
            if each_color == one_color:
                number += str(index)
    for index, each_color in enumerate(all_colors):
        if each_color == colors[2]:    
            number = str(int(number) * pow(10, index))
    temp = int(number)
    while temp // 10 > 0 and temp % 10 == 0:
        trailing_zeros += 1
        temp //= 10
    for metric_index in range(len(metric_prefix))[::-1]:
        if (metric_index * 3) <= trailing_zeros:
            number = number[:len(number) - metric_index * 3] 
            number += ' ' + metric_prefix[metric_index]
            return number
    
            
            
            

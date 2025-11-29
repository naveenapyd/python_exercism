def resistor_label(colors):
    all_colors = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
    if len(colors) == 1:
        return '0 ohms'
    number = ''
    for each_color in colors[:-1]:
        for index, value in enumerate(all_colors):
            if value == each_color:
                number += str(index)
    return multiplier(number) + ' ' + tolerance(colors[-1])
    
def tolerance(color):
    tolerance_color = ['grey', 'violet', 'blue', 'green', 'brown', 'red', 'gold', 'silver']
    tolerance_value = ['±0.05%', '±0.1%', '±0.25%', '±0.5%', '±1%', '±2%', '±5%', '±10%']
    for index, value in enumerate(tolerance_color):
        if value == color:
            return tolerance_value[index]

def multiplier(number):
    all_colors = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
    metric_prefix = ['ohms', 'kiloohms', 'megaohms', 'gigaohms']
    count_of_digits = 0
    number = str(int(number[:-1]) * pow(10, int(number[-1])))
    temp = int(number)
    while temp // 10 > 0:
         count_of_digits += 1
         temp //= 10
    for metric_index in range(len(metric_prefix))[::-1]:
         if metric_index * 3 <= count_of_digits:
             number = str(float(number) / pow(10, metric_index * 3))
             if number[-2:] == '.0':
                 number = str(int(float(number)))
             number += ' ' + metric_prefix[metric_index]
             return number
    
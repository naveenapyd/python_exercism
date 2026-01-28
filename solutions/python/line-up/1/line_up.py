def line_up(name, number):
    ordinals = ['st', 'nd', 'rd', 'th']
    if number % 10 == 1 and number % 100 != 11:
        return name + ', you are the ' + str(number) + ordinals[0] + ' customer we serve today. Thank you!' 
    elif number % 10 == 2 and number % 100 != 12:
        return name + ', you are the ' + str(number) + ordinals[1] + ' customer we serve today. Thank you!' 
    elif number % 10 == 3 and number % 100 != 13:
        return name + ', you are the ' + str(number) + ordinals[2] + ' customer we serve today. Thank you!' 
    else:
        return name + ', you are the ' + str(number) + ordinals[3] + ' customer we serve today. Thank you!'

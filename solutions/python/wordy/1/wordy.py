allowed_operations = ['plus', 'minus', 'multiplied', 'divided']

def validate_numbers_and_operators_sequence(num_op_list):
    for index, value in enumerate(num_op_list):
        if index % 2 == 0 and type(value) is not int:         
            # check for even indices; they should be numbers only
            raise ValueError('syntax error')
        if index % 2 != 0 and type(value) is int:
            # check for odd indices; they should be operations only
            raise ValueError('syntax error')
        if index % 2 != 0 and value not in allowed_operations:
            # check for operations; should be only allowed_operations
            raise ValueError('unknown operation')
    if len(num_op_list) % 2 == 0:
        # sequence should be number, operator, number, operator, number
        # if the length is even; it means there are only two - number, operator
        # and minimum three values are required to do calculation
        raise ValueError('syntax error')
                
def answer(question):
    number_str = ''
    list_of_numbers_and_operators = []
    char_to_ignore = ['What', 'is', 'by']
    for index, each_char in enumerate(question[:-1].split()):
        # in 'What is 5?', '5?'' becomes one element if split() is done
        # hence consider the question only till before '?'
        # also '?' can't be added in char_to_ignore list 
        # as split() will create elements based on space
        # so '?' can't be removed from '5?'
        if each_char in char_to_ignore:
            continue
        if each_char.isdigit() or each_char.startswith('-'):
            list_of_numbers_and_operators.append(int(each_char))
        else:
            list_of_numbers_and_operators.append(each_char)
    
    validate_numbers_and_operators_sequence(list_of_numbers_and_operators)

    if len(list_of_numbers_and_operators) == 1:
        return list_of_numbers_and_operators[0]

    if list_of_numbers_and_operators[1] == 'plus':
        result = list_of_numbers_and_operators[0] + list_of_numbers_and_operators [2]
    elif list_of_numbers_and_operators[1] == 'minus':
         result = list_of_numbers_and_operators[0] - list_of_numbers_and_operators [2]
    elif list_of_numbers_and_operators[1] == 'multiplied': 
        result = list_of_numbers_and_operators[0] * list_of_numbers_and_operators [2]
    elif list_of_numbers_and_operators[1] == 'divided':
        result = list_of_numbers_and_operators[0] // list_of_numbers_and_operators [2]
        
    for index, operator in enumerate(list_of_numbers_and_operators[3:]):
        if operator == 'plus':
            result += list_of_numbers_and_operators[3:][index + 1]
        elif operator == 'minus':
            result -= list_of_numbers_and_operators[3:][index + 1]
        elif operator == 'multiplied':
            result *= list_of_numbers_and_operators[3:][index + 1]
        elif operator == 'divided':
            result //= list_of_numbers_and_operators[3:][index + 1]
    return result
def decode(string):
    final_string = ''
    number = ''
    for index, char in enumerate(string):
        if index == 0 and char.isalpha():
            # edge case as index-1 for the first char will be out of range
            final_string += char
            continue
        if char.isdigit():
            number += char
        elif string[index-1].isdigit():
            # if the previous char is a number then the present char should be repeated that many times
            final_string += char * int(number)
            number = '' # reset for next iteration
        else:
            final_string += char
    return final_string

def encode(string):
    final_string = ''
    count = 1
    for index, char in enumerate(string):
        if index == len(string)-1:
            # edge case as index+1 for the last char will be out of range
            if char != string[index-1]:
                final_string += char
            if char == string[index-1]:
                final_string += str(count) + char
            break
        if char != string[index+1]:
            # when the char does not match with the next char, the count should be reset
            if count == 1:
                # if there is only one letter, then no need to add the number
                final_string += char
            else:
                final_string += str(count) + char
            count = 1
        if char == string[index+1]:
            count += 1
    return final_string

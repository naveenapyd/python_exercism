import string

def abbreviate(words):
    spl_char = string.punctuation
    # string.punctuation contains !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
    acronym = ''
    new_string = ''
    for letter in words:
        if letter == '-':
            new_string += ' '
        elif letter in spl_char:
            continue
        else:
            new_string += letter
    for index, letter in enumerate(new_string):
        if index == 0:
            acronym += letter.upper()
            continue
        if new_string[index-1] == ' ' and new_string[index] != ' ':
            # checks for multiple whitespaces
            acronym += letter.upper()
    return acronym
    

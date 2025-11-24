import string
alphabet = string.ascii_letters

def is_sum_zero(isbn):
    total_sum = 0
    for each_char in isbn:
        if each_char.isdigit():
            total_sum += int(each_char)
    if total_sum == 0:
        return True
    return False
        
def is_valid(isbn):
    isbn_without_dash = isbn.replace('-', '')
    if isbn_without_dash == '' or is_sum_zero(isbn_without_dash) or len(isbn_without_dash) != 10:
        return False
    for index, each_char in enumerate(isbn_without_dash):
        if each_char in alphabet and each_char != 'X':
            return False
        if each_char == 'X' and index != len(isbn_without_dash) - 1:
            return False
    result = 0
    for index, each_digit in enumerate(isbn_without_dash):
        if each_digit == 'X':
            result += 10 * (len(isbn_without_dash) - index)
        else:
            result += int(each_digit) * (len(isbn_without_dash) - index)
    if result % 11 == 0:
        return True
    return False
        

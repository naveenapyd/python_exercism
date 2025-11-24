def calculation(number):
    number_of_digits = len(str(abs(number)))
    sum_of_digits = 0
    while number > 0:
        last_digit = number % 10 
        sum_of_digits = sum_of_digits + (last_digit ** number_of_digits)
        number = int(number / 10)
    return sum_of_digits

def is_armstrong_number(number):
    number_of_digits = len(str(abs(number)))
    if(number_of_digits != 0):
        answer = calculation(number)
        if(answer == number):
            return True
        else:
            return False
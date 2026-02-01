''' VLQ '''

def encode(numbers):
    ''' The numbers list contains numbers in hexadecimal format.
    Step-1: Hexadecimeal numbers should be converted to decimal numbers.
    Step-2: Decimal numbers should be converted to Binary numbers (32-bit). Or can also directly do hex to binary.
    Step-3: Binary numbers should be split to 7-bit chunks.
    Step-4: Continuation flag should be added as the most significant bit (MSB).
    Step-5: 8-bit binary numbers are split into 4 digits each and converted to decimal numbers.
    Step-6: Decimal numbers should be converted to hexadecimal. '''

    vlq_hex_list = []
    for a_number in numbers:
        each_number = hex(a_number).upper()
        # converting int to str, as input '0x40' will be considered as 64
        # this needs to be converted to str representation - hex(int)
        only_digits = each_number[2:]
        # removing 0x in the beginning of every number
        hex_number = '0' * (8-len(only_digits)) + only_digits
        # adding the leading zeros till it becomes an eight digit number
        #print(hex_number)
        decimal_number = hex_to_decimal(hex_number)
        #print(f'encode : Decimal number is {decimal_number}')
        binary_number = decimal_to_binary(decimal_number)
        #print(f'encode : Binary number is {binary_number}')
        vlq_binary = continuation_flag(binary_number)
        #print(f'encode : Variable Length Quantity of Binary number with most significant bit is {vlq_binary}')
        vlq_hex = final_vlq(vlq_binary)
        #print(f'encode : Final VLQ - VLQ of hex number is {vlq_hex}')
        vlq_hex_list.extend(vlq_hex)
    converted_list = [int(a,16) for a in vlq_hex_list]
    return converted_list
    
def hex_to_decimal(each_number):
    # convert hexadecimal number to decimal number
    hex_digits = '0123456789ABCDEF'
    decimal_number = 0
    #print(each_number)
    for index, digit in enumerate(reversed(str(each_number))):
        hex_value = hex_digits.index(digit)
        #print(f'hex_to_decimal : Hexadecimal value of {digit} is {hex_value}')
        decimal_number += hex_value * (16 ** index)
        #print(f'hex_to_deciaml : Decimal number after each iteration is {decimal_number}')
    return decimal_number

def decimal_to_binary(decimal_number):
    # convert decimal number to binary number
    binary_number = ''
    if decimal_number == 0:
        return '0'
    while decimal_number > 0:
        #print(f'decimal_to_binary : Decimal number for each iteration is {decimal_number}')
        remainder = decimal_number % 2
        #print(f'decimal_to_binary : Remainder for each iteration is {remainder}')
        binary_number += str(remainder)
        #print(f'decimal_to_binary : Binary number for each iteration is {binary_number}')
        decimal_number //= 2
    return binary_number[::-1]

def continuation_flag(binary_number):
    # binary numbers are split into 7-bit chunks and most significant bit is added
    # depending on whether it is the last chunk or not
    # last chunk will have its most significant bit as 0
    # and others will have 1
    substrings = []
    for index in range(len(binary_number), -1, -7):
        # reverse order is required
        #print(f'continuation flag : index is {index}')
        start_index = max(0, index-7)
        #print(f'continuation flag : start_index is {start_index}')
        # determine the start index so that it doesn't go below zero
        # eg: 'abcdefghijklmnopqrstuvwx' - 24 characters
        # when index=24, it slices from 17:24 -> 'rstuvwx'
        # when index=17, it slices from 10:17 -> 'klmnopq'
        # when index=10, it slices from 3:10 -> 'defghij'
        # when index=3, it slices from 0:3 -> 'abc' (length 3)
        if start_index == index:
            break
        binary_number_split = binary_number[start_index : index]
        #print(f'continuation_flag : VLQ Binary is {binary_number_split}')
        while len(binary_number_split) < 7:
            # adding zeros until the 7 digits
            binary_number_split = '0' + binary_number_split
        substrings.append(binary_number_split)
    for index in range(len(substrings)):
        # add the most significant bit
        if index == 0:
          substrings[index] = '0' + substrings[index]
        else:
          substrings[index] = '1' + substrings[index]
    return substrings[::-1]

def final_vlq(vlq_binary):
    # conversion of binary vlq to hexadecimal vlq is done
    binary_split_list = []
    for eight_digit_string in vlq_binary:
        # splitting the eight digits to two four digits
        first_four_digit_string = eight_digit_string[:4]
        binary_split_list.append(first_four_digit_string)
        second_four_digit_string = eight_digit_string[4:]
        binary_split_list.append(second_four_digit_string)
    hex_vlq_digits = []
    hex_digits = '0123456789ABCDEF'
    for every_quad in binary_split_list:
        # convert the 4 digits to a decimal number
        # convert this decimal to hexadecimal number
        #print(f'Four digits are {every_quad}')
        decimal_value = 0
        for index, value in enumerate(every_quad):
            #print(f'Index and value of the four digits are {index} and {value}')
            decimal_value += (2 ** (len(every_quad)-1 - index)) * int(value)
            # len - index is done above for the reverse order
            #print(f'Decimal value is {decimal_value}')
        if decimal_value == 0:
            hex_vlq_digits.append(str(decimal_value))
        else:
            while decimal_value > 0:
                remainder = decimal_value % 16
                hex_digit = hex_digits[remainder]
                #print(f'Hexadecimal value is {hex_digit}')
                decimal_value //= 16
            hex_vlq_digits.append(str(hex_digit))
    hex_vlq = []
    for index in range(0, len(hex_vlq_digits), 2):
        hex_vlq.append('0x' + hex_vlq_digits[index] + hex_vlq_digits[index + 1])
    return hex_vlq

def decode(bytes_):
    '''The bytes_ list contains VLQ encoding of hexadecimal numbers.
    Step-1: Hexadecimal VLQ should be converted to binary format - hex to decimal to binary.
    Step-2: Extract 7-bit chunks from the binary format.
    Step-3: Concatenate the 7-bit chunks and convert to decimal format.
    Step-4: Convert the decimal format to hexadecimal number.'''

    binary_bytes_list = []
    final_list = []
    for idx, a_number in enumerate(bytes_):
        byte = hex(a_number).upper()
        only_digits = byte[2:]
        # removing 0x in the beginning of every byte
        decimal_bytes = hex_to_decimal(only_digits)
        binary_bytes = decimal_to_binary(decimal_bytes)
        binary_eight_digits = '0' * (8-len(binary_bytes)) + binary_bytes
        # adding the leading zeros till it becomes an eight digit number
        if idx == len(bytes_) - 1 and binary_eight_digits[0] == '1':
            # last index value has MSB 1, then it means that there should be one more hex number
            # if there isn't any more hex number after this, it means it is incomplete
            raise ValueError('incomplete sequence')
        binary_without_msb = binary_eight_digits[1:]
        binary_bytes_list.append(binary_without_msb)
        if binary_eight_digits[0] == '0':
            # this checks end of one sequence i.e., with msb 0, decodes it, and then goes to the next sequence until it finds another msb 0
            concatenation = ''
            for value in binary_bytes_list:
                # concatenating all values in the list
                concatenation += value
            # print(f'Binary Concatenation: {concatenation}')
            decimal_number = binary_to_decimal(concatenation)
            # print(f'Decimal number: {decimal_number}')
            hex_number = decimal_to_hex(decimal_number)
            final_list.append(int(hex_number, 16))
            binary_bytes_list = []
    return final_list

def binary_to_decimal(concatenation):
    decimal_value = 0
    for index, value in enumerate(concatenation):
        decimal_value += (2 ** (len(concatenation)-1 - index)) * int(value)
    return decimal_value

def decimal_to_hex(decimal_number):
    hex_digits = '0123456789ABCDEF'
    hex_string = ''
    if decimal_number == 0:
        return '0'
    else:
        while decimal_number > 0:
            remainder = decimal_number % 16
            hex_string = hex_digits[remainder] + hex_string
            # prepend digits for each iteration
            # print(f'Hexadecimal value is {hex_string}')
            decimal_number //= 16
            # print(f'Decimal number becomes: {decimal_number}')
    return hex_string

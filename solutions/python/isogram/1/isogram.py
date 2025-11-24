def is_isogram(string):
    string_without_special_char = ''
    for each_letter in string:
        if each_letter.isalpha():
            string_without_special_char += each_letter   
    for each_letter in string_without_special_char:
        if string_without_special_char.lower().count(each_letter) > 1:
            return False
    return True
    

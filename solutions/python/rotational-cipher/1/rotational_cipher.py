import string
alphabet_lowercase = string.ascii_lowercase
alphabet_uppercase = string.ascii_uppercase

def rotate(text, key):
    new_text = ''
    for each_char in text:
        if each_char in alphabet_lowercase:
            index = alphabet_lowercase.index(each_char)
            if index + key <= 25:
                new_text += alphabet_lowercase[(index + key)]
            else:
                new_text += alphabet_lowercase[index + key - 26]
        elif each_char in alphabet_uppercase:
            index = alphabet_uppercase.index(each_char)
            if index + key <= 25:
                new_text += alphabet_uppercase[index + key]
            else:
                new_text += alphabet_uppercase[index + key - 26]
        else:
            new_text += each_char
    return new_text
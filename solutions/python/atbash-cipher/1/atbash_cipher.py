import string
alphabet_lower = string.ascii_lowercase
digits = '0123456789'

def encode(plain_text):
    plain_text_lower = plain_text.lower()
    new_text = ''
    for each_char in plain_text_lower:
        if each_char in alphabet_lower:
            index_of_new_char = len(alphabet_lower) - 1 - alphabet_lower.index(each_char)
            new_text += alphabet_lower[index_of_new_char]
        if each_char in digits:
            new_text += each_char
    ciphered_text = ''
    for index in range(0, len(new_text), 5):
        substring = new_text[index : index + 5]
        ciphered_text += substring + ' '
    return ciphered_text.strip()

def decode(ciphered_text):
    ciphered_text_lower = ciphered_text.lower()
    plain_text = ''
    for each_char in ciphered_text_lower:
        if each_char in alphabet_lower:
            index_of_new_char = len(alphabet_lower) - 1 - alphabet_lower.index(each_char)
            plain_text += alphabet_lower[index_of_new_char]
        if each_char in digits:
            plain_text += each_char
    return plain_text
        

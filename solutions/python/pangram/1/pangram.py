import string 
alphabet = string.ascii_lowercase

def is_pangram(sentence):
    sentence_without_space = ''
    for each_letter in sentence:
        if each_letter.isalpha():
            sentence_without_space = sentence_without_space + each_letter
    sentence_without_space = sentence_without_space.lower()
    for each_letter in alphabet:
        if each_letter not in sentence_without_space:
            return False
    return True

def word(text):
  vowels = 'aeiou'
  if text[0] in vowels or text[:2] == 'xr' or text[:2] == 'yt':
    return text + 'ay'
  index_of_text = 0
  while index_of_text < len(text) and text[index_of_text] not in vowels and text[index_of_text : index_of_text + 2] != 'qu':
      if text[index_of_text] == 'y' and index_of_text != 0:
          break
      index_of_text += 1 
  if text[index_of_text] == 'y':
    before_y = text[:index_of_text]
    from_y = text[index_of_text:]
    return from_y + before_y + 'ay'
  if text[index_of_text : index_of_text + 2] == 'qu':
    till_qu = text[:index_of_text + 2]
    after_qu = text[index_of_text + 2:]
    return after_qu + till_qu + 'ay'
  if text[index_of_text] in vowels:
    before_vowel = text[:index_of_text]
    from_vowel = text[index_of_text:]
    return from_vowel + before_vowel + 'ay'
def translate(text):
    split_phrase = text.split()
    #i = 0
    result = ''
    #while i < len(split_phrase):
    for phrase in split_phrase:
        result = result + word(phrase) + ' '
    return result[:-1]
  
def find_anagrams(word, candidates):
    result = []
    for each_word in candidates: 
        if word.lower() == each_word.lower():
            # the exact word should not be in the output
            continue
        each_word_sorted = ''.join(sorted(each_word.lower())) 
        # sorted returns a list of strings withh each letter as a string
        # eg: dcab will be returned as ['a','b','c','d']
        # join will make it into a string, as 'abcd'
        word_sorted = ''.join(sorted(word.lower()))
        if word_sorted == each_word_sorted:
            result.append(each_word)
    return result
                    

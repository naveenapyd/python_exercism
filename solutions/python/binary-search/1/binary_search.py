def find(search_list, value):
    for index, num in enumerate(search_list):
        if num == value:
            return index
    raise ValueError('value not in array')

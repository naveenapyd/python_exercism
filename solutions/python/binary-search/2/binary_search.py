def find(search_list, value):
    if len(search_list) == 0:
        raise ValueError('value not in array')
    low = 0
    high = len(search_list) - 1 # the -1 keeps the list index in range
    while low <= high:
        mid = (low + high) // 2
        if search_list[mid] == value:
            return mid
        elif search_list[mid] < value:
            low = mid + 1
        elif search_list[mid] > value:
            high = mid - 1
    raise ValueError('value not in array')

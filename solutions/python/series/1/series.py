def slices(series, length):
    if length == 0:
        raise ValueError('slice length cannot be zero')
    if length < 0:
        raise ValueError('slice length cannot be negative')
    if len(series) == 0:
        raise ValueError('series cannot be empty')
    if length > len(series):
        raise ValueError('slice length cannot be greater than series length')
    list_of_slices = []
    for index in range(len(series)):
        slice = ''
        if len(series[index : len(series)]) < length:
            # checks if the slice len is less than the required length
            break
        slice = series[index : index+length]
        list_of_slices.append(slice)
    return list_of_slices
        

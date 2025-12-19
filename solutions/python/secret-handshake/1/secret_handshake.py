def commands(binary_str):
    code = []
    for index in range(len(binary_str)-1,0,-1):
        if binary_str[index] == '1':
            if index == 4:
                code.append('wink')
            if index == 3:
                code.append('double blink')
            if index == 2:
                code.append('close your eyes')
            if index == 1:
                code.append('jump')
    if binary_str[0] == '1':
        return code[::-1]
    return code
       
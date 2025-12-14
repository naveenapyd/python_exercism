def is_paired(input_string):
    if len(input_string) == 0:
        # if the input is empty
        print(True)
    brackets_stack = []
    for char in input_string:
        if char == '(' or char == '[' or char == '{':
            # storing all opening brackets in the list - stack
            brackets_stack.append(char)
        elif char == ')':
            # check for closing brackets
            # when a closing bracket is found, pop the opening bracket from the stack and check if it matches with the found closing bracket
            # check for length of the stack as well; because if a closing bracket is present without an opening bracket, then the result should be False
            if len(brackets_stack) == 0 or brackets_stack.pop() != '(':
                return False
        elif char == ']':
            if len(brackets_stack) == 0 or brackets_stack.pop() != '[':
                return False
        elif char == '}':
            if len(brackets_stack) == 0 or brackets_stack.pop() != '{':
                return False 
    # finally, when the stack becomes empty, it means that all brackets are matched, so return true
    # if the brackets are not matched in the stack, meaning only opening brackets are left with no closing brackets, so return False
    return len(brackets_stack) == 0
    

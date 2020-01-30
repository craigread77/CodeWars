def valid_parentheses(string):
    
    i = 0
    for count, char in enumerate(string):
        if i < 0:
            return False
        if char == '(':
            i += 1
        elif char == ')':
            i -= 1
    
    return i == 0
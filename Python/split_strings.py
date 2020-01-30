def solutions(s):
    result = []

    if s == '':
        return result

    # If s contains odd number of chars
    if len(s) % 2 == 1:
        s += '_'

    section = 0
    next_section = 2

    while next_section <= len(s):
        result.append(s[section:next_section])
        section += 2
        next_section += 2

    return result


print(solutions('asdfasdfg'))

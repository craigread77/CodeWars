import re
def increment_string(strng):
    

    if strng == '':
        return '1'

    elif strng[len(strng)-1].isalpha():
        return strng + '1'


    stringRegex = re.compile(r'([A-Za-z/.\@#$%^&*,!`]*)(0*)(\d*)$')

    if stringRegex.match(strng) != None:

        word = stringRegex.match(strng).groups()[0]
        zeroes = stringRegex.match(strng).groups()[1]
        num = stringRegex.match(strng).groups()[2]
    else:
        return None

    if len(num) < 1:
        zeroes = zeroes[:len(zeroes)-1] + '1'

    else:
        num_digits = len(num)
        num = int(num)
        num += 1
        num_digits_after = len(str(num))


        if num_digits != num_digits_after:
            if len(zeroes) > 0:
                zeroes = zeroes [1:]




    return word + zeroes + str(num)

print(increment_string('foo00'))

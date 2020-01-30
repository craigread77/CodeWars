import re

def disemvowel(string):
    return ''.join(re.findall(r'[^aeiou]', string, re.IGNORECASE))

print(disemvowel('my name is hannah and I am a troll!'))

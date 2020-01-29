def anagrams(word, words):
    matches = []
    word = sorted(word.lower())

    for count, value in enumerate(words):
        if sorted(value.lower()) == word:
            matches.append(value)

    return matches

    

def anagrams(word, words):
    return [item for item in words if sorted(item.lower())==sorted(word.lower())]
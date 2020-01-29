def goodVsEvil(good, evil):
    goodWeights = [1, 2, 3, 3, 4, 10]
    evilWeights = [1, 2, 2, 2, 3, 5, 10]
    
    goodPower = sum([int(value) * goodWeights[count] for count, value in enumerate(good.split(' '))])
    evilPower = sum([int(value) * evilWeights[count] for count, value in enumerate(evil.split(' '))])

    
    if goodPower == evilPower:
        return "Battle Result: No victor on this battle field"

    elif max(goodPower, evilPower) == goodPower:
        return "Battle Result: Good triumphs over Evil"
    else:
        return "Battle Result: Evil eradicates all trace of Good"

print(goodVsEvil('1 1 1 1 1 1', '1 1 1 1 1 1 1'))
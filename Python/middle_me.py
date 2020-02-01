def middleMe(N, X, Y):
    if N % 2 == 1:
        return X
    else:
        return '{0}{1}{2}'.format(Y * int(N/2), X, Y * int(N/2))
        
print(middleMe(10, 'A', '*'))

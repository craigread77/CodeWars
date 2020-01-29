# def who_is_next(names, r):
    
#     for i in range(r):
#         names.append(names[i])
#         names.append(names[i])

#     #return names[len(names)-1:]
#     return names
    

names = ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]


def who_is_next(names, r):
    n = len(names)
    i = 1
    while n < r:
        r -= n
        n *= 2
        i *= 2
    return names[(r - 1) // i]


print(who_is_next(names, 10))
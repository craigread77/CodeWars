def array_diff(a, b):
    return [num for num in a if num not in b]

print(array_diff([1,2,2,2,3], [2]))
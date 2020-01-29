def find_even_index(arr):
    
    for count, value in enumerate(arr):
        if sum(arr[:count]) == sum(arr[count+1:]):
            return count

    return -1

print(find_even_index([1,2,3,4,3,2,1]))


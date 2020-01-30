def traffic_count(array):
    max_cars = []
    hours = ['4:00pm', '5:00pm', '6:00pm', '7:00pm']
    for i in range(4):
        max_cars.append(max(array[i * 6: (i + 1) * 6]))
    
    return [(hours[i], max_cars[i]) for i in range(4)]

print(traffic_count([23,24,34,45,43,23,57,34,65,12,19,45, 54,65,54,43,89,48,42,55,22,69,23,93]))
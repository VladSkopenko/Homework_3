points = {
    (0, 1): 2,
    (0, 2): 3.8,
    (0, 3): 2.7,
    (1, 2): 2.5,
    (1, 3): 4.1,
    (2, 3): 3.9,
}


def calculate_distance(coordinates):
    dis = 0
    if len(coordinates) == 0 or len(coordinates) == 1:
        return 0        
    else:
        for key , val in points.items():
            if key in coordinates:
                dis += val
        return dis
    
print(calculate_distance((1,2,3,4,5)))
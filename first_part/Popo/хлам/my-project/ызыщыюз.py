def split_list(grade):
    suma_grade = sum(grade)
    mid_num = suma_grade / len(grade)
    list_low = []
    list_big = []
    for ai in range(len(grade)):
        if ai <= mid_num :
            list_low += ai
        else:
            list_big += ai
    return list_low, list_big
    
        
split_list([1,2,3,4,5,6,7,8])
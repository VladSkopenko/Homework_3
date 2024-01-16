# Порахувати суму всіх чисел через рекурсію
# 10 -> 10 + 9 + 8 + 7 + ... + 1


def rec_sum(n):
    if n == 0 :
        return 0
    elif n == 1:
        return 1
    else:
        return n + rec_sum(n - 1) 
    


print(rec_sum(5))
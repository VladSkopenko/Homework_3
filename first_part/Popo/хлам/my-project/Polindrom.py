# Скласти програму, яка вводить цілі k, l.
# Якщо вони не рівні, то менше з них замінюється більшим, інакше обидва замінюються на 0.

while True:
    try:
        k = int(input("Enter k:"))
        l = int(input("Enter l "))
        if  k == l:
            k = 0
            l = 0 
        else:
            if k < l:
                k = l
            elif l < k:
                l = k
        print(k,l)
    except ValueError:
        print("Enter number pls")

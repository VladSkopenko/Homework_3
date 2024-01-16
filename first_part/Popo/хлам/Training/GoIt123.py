# Написати функцію для визначення, чи є число простим?

num  = input("Enter >>>")


def the_simpicity(num):
    if int(num) <= 1:
        return print("num is less or quals 1 ")
    for (nu) in range(2,int(num)):
        if int(num) % int(nu) == 0:
            return False , print("Num is not simple")
    return print("Simple num is True"), True


the_simpicity(num)
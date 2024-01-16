# Перевірити чи в 3-х значному числі всі цифри різні? І чи є тільки 2 однакових числа?
while True:
    try:
        num = int(input("Enter 3 digit number "))
        n3 = num % 10
        n2 = num // 10 % 10 
        n1 = num // 100 % 10
    
        if n3 != n1 and n3 != n2 and n2 != n1:
            print("All the numbers difference")
        elif n3 == n1 and n3 != n2 :
            print("Two numbers are Equal")
        elif n3 == n2 and n3 != n1 :
            print("Two numbers are Equal")
        elif n1 == n2 and n1 != n3:
            print("Two numbers are Equal")
        else:
            print("All the nubmers Equal")
    except ValueError:
        print(f"is not number")
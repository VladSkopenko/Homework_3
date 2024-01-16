# Скласти програму обчислення суми модулів трьох дійсних чисел
print("Вітаю ця программа є непотрібна але вона може  порахувати вам суму модулів трех чисел")
import math


while True:
    numbers_1 = int(input("Ввідіть якесь  число бажано від'ємне"))
    numbers_1 = math.fabs(numbers_1)

    numbers_2 = int(input("Ввідіть якесь  число бажано від'ємне "))
    numbers_2 = math.fabs(numbers_2)

    numbers_3 = int(input("Ввідіть якесь  число бажано від'ємне "))
    numbers_3 = math.fabs(numbers_3)

    suma_modyliv = numbers_3 + numbers_1 + numbers_2
    print(f"Сума модулів цих чисел дорівнює:{suma_modyliv}")

print("Вітаю друже це программа яка допоможе тобі вирахувати площу,діаметр  та довжину кола знаючи його радіус")

import math


while True:
    radius_of_a_circle = float(input("Введіть будь ласка радіус кола/Please enter the radius of the circle:"))
    area_circle = math.pi * radius_of_a_circle **2
    diametr_circle = 2 * radius_of_a_circle
    long_circle = 2 *math.pi * radius_of_a_circle
      
    print(f"Довжина кола дорівнює:{long_circle}")  
    print(f"Площа кола дорівнює:{area_circle}")
    print(f"Діаметр кола дорівнює{diametr_circle}")

    
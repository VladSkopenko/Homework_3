print("Ця программа виводить на ваш екран середне арифметичне усіх цифр з уводенного вами 4-х значного числа наприклад 1111")

while True:
    mine_number = int(input("Введіть чоторьох значне число:"))
    number_4 = mine_number % 10
    number_3 = mine_number // 10 % 10 
    number_2 = mine_number // 100 % 10 
    number_1 = mine_number // 1000 % 10 
    average_afirmetics = (number_3 + number_4 + number_2 + number_1) / 4
    print(f"Ось будь ласка середне арифметичне чотирьох  цифр  {average_afirmetics}")
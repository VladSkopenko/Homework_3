try:
    while True:
        operand_1 = int(input("Enter operand:"))
        operator = str(input("Enter operator:"))
        if operator == "-":
             operand_2 = int(input("Enter operand:"))
             operator = str(input("Enter operator:"))
             result = operand_1 - operand_2
             if operator == "=" : 
                 print(result)
                 break
             else:
                 print("Ви ввели некоректний оператор спробуйте ще раз")
                 continue
                     
        elif operator == "+" : 
             operand_2 = int(input("Enter operand:"))
             operator = str(input("Enter operator:"))
             result = operand_1 + operand_2
             if operator == "=" :
                 print(result)
                 break
             else: 
                 print("Введіть будь ласка = для отримання результату")   
                 continue        
        elif operator == "*" : 
             operand_2 = int(input("Enter operand:"))
             operator = str(input("Enter operator:"))
             result = operand_1 * operand_2
             if operator == "=" :
                 print(result)
                 break
              
        elif operator == "/" :
             operand_2 = int(input("Enter operand:"))
             operator = str(input("Enter operator:"))
             result = operand_1 / operand_2
             if operator == "=" :
                 print(result)
                 break
             else:
                 print("Введіть будь ласка = для отримання результату")   
                 continue  
        else:
            print("Вы двічі ввели число , будь ласка спробуйте ще раз")
            continue
except ValueError:
    print("Сталася бида")
except TypeError: 
    print("Beda")
   
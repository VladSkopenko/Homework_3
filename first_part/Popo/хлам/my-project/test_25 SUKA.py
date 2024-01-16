result = 0
operand = 0
operator = None
wait_for_number = True
if result == None:
    operand + result
while True: 
    user_enter = input(">>>")
    if user_enter == "=":
        print(f"Результат  {result}")
        break
    elif wait_for_number:
        try:
            operand = int(user_enter)
            if result == None:
                result += operand
                result = True      
        except ValueError:
            print(f"{user_enter} не є номером")
            continue
    else:
        if user_enter not in ("+", "-", "*", "/"):
            print(f"{user_enter} не є матиматичним знаком")
            continue
        operator = user_enter
        wait_for_number = True
        if operator == "+" :
            result +=  operand
        elif operator == "-" :
            result -= operand
        elif operator == "*" :
            result *= operand
        elif operator == "/" :
            if operand == 0 :
                print(f"Неможливо ділити на нуль")
                continue
            result /= operand

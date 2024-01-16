operator = None
operand = None
result = None
wait_for_number = True
while True:
    if wait_for_number:
        try:
            operand = float(input())
            if operand == "=":
                print(result)
                break
            if operator == None :
                result = operand
            if operator == "-" :
                result -= operand
            elif operator == "+" :
                result += operand
            elif operator == "/" :
                result /= operand
            elif operator == "*" :
                result *= operand
            wait_for_number = False
        except ValueError:
            print(f"Введи число а не билибирду свою . ")
        except ZeroDivisionError:
            print(f"На нуль  ділити неможна голова")
    else:
        operator = input("Введи знак дії математичний >>>")
        if operator == "=" :
            print(result)
            break
        elif operator == "*" or operator == "-" or operator == "+" or operator == "/":
            wait_for_number = True
            continue
        else:
            print("Введи знак йомайо * - + / or = ")
            
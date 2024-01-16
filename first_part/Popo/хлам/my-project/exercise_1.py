
result = None
operand = None
operator = None
wait_for_number = True

while True:
    try:
        user_input = input()
        if user_input == "=":
            if operand is not None and operator is not None:
                if operator == '+':
                    result += operand
                elif operator == '-':
                    result -= operand
                elif operator == '*':
                    result *= operand
                elif operator == '/':
                    if operand == 0:
                        print("Division by zero is not allowed.")
                        break
                    result /= operand
            else:
                print("Invalid input. Please try again.")
                continue
            print("Result:", result)
            break
        elif wait_for_number:
            operand = float(user_input)
            wait_for_number = False
        else:
            if operator(user_input):
                if operator is not None:
                    print("Operator already provided. Please enter a number.")
                    continue
                operator = user_input
                wait_for_number = True
            else:
                print(f"'{user_input}' is not '+', '-', '*', or '/'. Try again.")
    except ValueError:
        print(f"'{user_input}' is not a valid number. Try again.")
    except ZeroDivisionError:
        print("Division by zero is not allowed.")
        break

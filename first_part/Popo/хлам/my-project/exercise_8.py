print("Вітаю ця программа переводить час із секунд в години хвилини та секунди")

while True:
    total_second = int(input("Введіть кількість секунд:"))
    hours = total_second // 3600
    last_second = total_second % 3600
    minute =  last_second // 60 
    more_last_second = total_second % 60 
    second = more_last_second // 1

    print(f"{total_second} Секунд дорівнює {hours}часам {minute}хвилинам та {second}секундам")
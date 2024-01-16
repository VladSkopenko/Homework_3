# Нехай ми маємо текстовий файл, який містить дані з місячною заробітною платою по кожному розробнику компанії.

# Приклад файлу:

# Alex Korp,3000
# Nikita Borisenko,2000
# Sitarama Raju,1000
# Як бачимо, структура файлу – це прізвище розробника та значення його заробітної плати, розділеної комою.

# Розробіть функцію total_salary(path) (параметр path - шлях до файлу), 
#яка буде розбирати текстовий файл і повертати загальну суму заробітної плати всіх розробників компанії.

# Вимоги до завдання:

# функція total_salary повертає значення типу float
# для читання файлу функція total_salary використовує лише метод readline
# ми поки що не використовуємо менеджер контексту with

def total_salary(path):
    total = 0.0
    file = open(path , "r")
    line = file.readline()
    while line:
        parts = line.split(',')
        if len(parts) >= 2:
            try:
                salary = float(int(parts[1].strip()))
                total += salary
            except ValueError :
                print("Хуйня")
        line = file.readline()
    file.close()
    return total


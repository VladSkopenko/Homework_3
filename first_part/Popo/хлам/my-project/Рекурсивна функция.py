def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
print(f"Факториал  веведенего числа дорівнює" , factorial(7))
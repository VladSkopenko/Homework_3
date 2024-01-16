def fib(n):
    if n == 0:
        return 0 
    elif n == 1 or n == 2:
        return 1
    else:
        n = fib(n-1) + fib(n-2)
        return n 

print(fib(10))
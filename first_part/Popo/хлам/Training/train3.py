# Функція приймає рядок, а повертає словник, де ключ це символ рядка, а значення код ASCII
# {'key': 'value'}
# hello world
a = input("Enter something >>>")

def fun(a):
    dict = {}
    for ch in a:
        dict[ch] = ord(ch)
    return dict

print(fun(a))
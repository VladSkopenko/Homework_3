sum = 0
while True:
    num = int(input("Enter integer (0 for output): "))
    if num == 0:
        break
    for i in range(num + 1):
        if i >= 0 and i % 2 == 0:     
         sum = sum + i
         print(sum)
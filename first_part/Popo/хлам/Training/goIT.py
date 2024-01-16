# У нас є строка: a = "lsj94ks6d231* !9#".
# Потрібно створити список в якому будуть тільки цифри


a = "lsj94ks6d231* !9#"
result_list = []
for ch in a :
    if  ch.isdigit():
        result_list.append(ch)
    
print(result_list)
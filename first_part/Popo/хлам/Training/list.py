def lookup_key(data, value):
    listok = []
    if len(data) == 0 :
        return []
    for key , val in data.items():
        if val == value:
            listok.append(key)
    return listok
    


data = {
    "1":1,
    "2":2,
    "3":3,
    "4":1,
    "5":2
}

value = 1

print(lookup_key(data, value))
# Повернімося до завдання з пункту 8 для розрахунку площі. Ширина та висота задані у рядковому вигляді. 
# Необхідно, як і раніше, розрахувати площу, але потрібно рядковий тип перетворити на чисельний (float) при розрахунку площі area.
# Не забудьте також додати до змінної show рядок з наступним шаблоном: 'With width <значення ширини> and length <значення довжини> of the room, its a

length = "12.5"
width = "10.1"
area = float(length) * float(width)
show = f"With width {width} and length {length} of the room, its area is equal to {area}"
print(area)
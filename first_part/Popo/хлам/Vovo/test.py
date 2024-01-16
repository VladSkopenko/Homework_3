# Для кава-брейків на конференції закуплено:
# х круасанів, у стаканчиків, z упаковок кави.
# Ціна круасана $1.04, ціна стаканчика - $0.34, ціна упаковки кави $4.42
# Скласти програму, яка обчислює,
# скільки повних доларів пішло на закупівлю їжі для кава-брейків, і яка її вартість у центах.

a_croissant = float(input("Введіть кількість круасанів:"))
cup = float(input("Введіть кількість стаканчиків: "))
z = float(input("Введіть кількість упаковок кави:"))

price_x = 1.04
price_cup = 0.34
price_z = 4.42


cost_a_croissant_dollars = a_croissant * price_x
cost_a_croissant_dollars = int(cost_a_croissant_dollars)

cost_a_croissant_cent = (a_croissant * price_x - cost_a_croissant_dollars) * 100
cost_a_croissant_cent = int(cost_a_croissant_cent)

cost_cup = cup * price_cup
cost_cup_dol = int(cost_cup)
cost_cup_cent = (cup * price_cup - cost_cup_dol) * 100
cost_cup_cent = int(cost_cup_cent)

print(f'Ціна за круасани дорівнює {cost_a_croissant_dollars} Доларів та {cost_a_croissant_cent} центів')



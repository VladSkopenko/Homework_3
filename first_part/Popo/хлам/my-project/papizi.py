items = ["2 eggs", "1 liter sugar", "1 tsp salt", "vinegar"]






def format_ingredients(items):
    a = ", ".join(items[:-1])
    a += " and " + items[-1]
    print(a)
    


format_ingredients(items)
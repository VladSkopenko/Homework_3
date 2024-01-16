items = ["2 eggs", "1 liter sugar", "1 tsp salt", "vinegar"]
new_str = ""
def format_ingredients(items):
    new_str = ""
    if len(items) == 0 or len(items) == 1:
        str_new = items.join(items)
    else:
        items = ", ".join(items[:-1])
        items = items + " and " + items[-1]
        
    print(items)
    return items

format_ingredients(items)
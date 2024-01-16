def is_valid_pin_codes(pin_codes):
    if len(pin_codes) == 0:
        return False
    if len(pin_codes) != len(set(pin_codes)):
        return False
    for i in pin_codes:
        long = len(i)
        if long != 4:
            return False
        if not i.isdigit():
            return False
    return True 
    
    
    
print(is_valid_pin_codes(["2134","1111","1111"]))
print(is_valid_pin_codes(["ferf","1234"]))


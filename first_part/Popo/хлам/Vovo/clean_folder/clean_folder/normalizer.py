import re


CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")


TRANS = {}


for c , i  in  zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[ord(c)] = i
    TRANS[ord(c.upper())] = i.upper()


def normalize(name):
    translate_name = re.sub(r'[^\w.]+', name.translate(TRANS))
    return translate_name
from textwrap import wrap

dictionary = {
   "2c": "  ", "36": ",<", "37": ".>", "38": "/?", 
   "27": "0)", "1e": "1!", "1f": "2@", "20": "3#", "21": "4$", 
   "22": "5%", "23": "6^", "24&": "7",  "25": "8*", "26": "9(", 
   "33": ";:", "2e": "=+", "2d": "-_",  "04": "aA", "05": "bB",
   "06": "cC", "07": "dD", "08": "eE", "09": "fF", "0a": "gG",
   "0b": "hH", "0c": "iI", "0d": "jJ", "0e": "kK", "0f": "lL",
   "10": "mM", "11": "nN", "12": "oO", "13": "pP", "14": "qQ",
   "15": "rR", "16": "sS", "17": "tT", "18": "uU", "19": "vV",
   "1a": "wW", "1b": "xX", "1c": "yY", "1d": "zZ", "2f": "[{",
   "30": "]}", "2a": ["DEL"]*2, "50": ["LEFT"]*2, "4f": ["RIGHT"]*2,
}

def maps(key):
    return dictionary.get(key, '')

text = open('capdata').read().split()
data = [wrap(_, 2) for _ in text]

results = [
    maps(_[2])[1] if _[0] == '02'
    else maps(_[2])[0] for _ in data if maps(_[2])
]

element = [''] * 3000
pointer = 0

for key in results:
    if key == 'LEFT':
        pointer -= 1
    elif key == 'RIGHT':
        if element[pointer]:
            pointer += 1
    elif key == 'DEL':
        element.pop(pointer)
    else:
        element = element[:pointer] + [key] + element[pointer:]
        pointer += 1

print(''.join(element))

import re


def real_numbers(list):
    mylist = []
    for number in list:
        if re.match(r"^\s*[+-]?(\d+(.\d+)?)([eE][+-]?\d+)?\s*$", number):
            mylist.append("LEGAL")
        else:
            mylist.append("ILLEGAL")
    return mylist


print(real_numbers(['1.5e+2', '3.', '1.1.1', '1+e5']))

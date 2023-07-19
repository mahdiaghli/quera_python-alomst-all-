import os


def explore(ttype, address):
    ttype = '.' + ttype
    tup = list(os.walk(address))
    dict = {}
    for path in tup:
        counter = 0
        for str in path[2]:
            if ttype.lower() in str.lower():
                counter += 1
        if counter != 0:
            dict[path[0]] = counter
    return dict


print(explore("py", "../pythonProject1"))


def combet(SAliB_format, Sajjad_format, path):
    salib = explore("SAliB_format", path)
    sajjad = explore("Sajjad_format", path)

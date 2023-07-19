import os


def explore(ttype, address):
    ttype = '.' + ttype
    tup = list(os.walk(address))
    dict = {}
    dict2 = {}
    for path in tup:
        counter = 0
        for str in path[2]:
            if ttype.lower() in str.lower():
                counter += 1
        if counter != 0:
            dict[path[0]] = counter
    return dict


print(explore("py", "../os"))


def combet(SAliB_format, Sajjad_format, path):
    salib = explore("SAliB_format", path)
    SAliB_format = '.' + SAliB_format
    tup = list(os.walk(path))
    dict = {}
    mylist = []
    for tupin in tup:
        counter = 0
        for str in tupin[2]:
            if SAliB_format.lower() in str.lower():
                counter += 1
        if counter != 0:
            dict[tupin[0]] = counter

    numSalib = sum(salib.values())
    mylist = []
    for tupin in tup:
        for name in tupin[2]:
            name = name
    sajjad = explore("Sajjad_format", path)
    numSajjad = sum(sajjad.values())
    if numSajjad >= numSalib:
        print("Win! Normally!")

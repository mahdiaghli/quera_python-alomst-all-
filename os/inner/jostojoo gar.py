import os


def explore(ttype, address):
    number = 0
    dict = {}
    mylist = list(os.walk(address))
    for file in mylist[0][2]:
        if ttype in file:
            number = number + 1

    dict[mylist[0][0]] = number

    for folder in mylist[0][1]:
        number = 0
        mylist2 = list(os.walk(folder))
        for file in mylist2[0][2]:
            if ttype in file:
                number = number + 1
        dict[mylist2[0][0]] = number

    print(dict)


explore("py", "../os")
